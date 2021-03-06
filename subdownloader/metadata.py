# Copyright (c) 2017 SubDownloader Developers - See COPYING - GPLv3

import logging
import os

log = logging.getLogger('subdownloader.modules.metadata')


class MetadataVideoTrack(object):
    """
    Instances of this class collect some metadata of a video track.
    Only metadata is stored. It is meant to be attached to an actual video.
    """
    def __init__(self, duration_ms, framerate):
        """
        Create a new MetadataVideoTrack instance.
        :param duration_ms: Duration of the video track (in milliseconds)
        :param framerate: Frame rate of the video track (in frames per second)
        """
        self._duration_ms = duration_ms
        self._framerate = framerate

    def get_framerate(self):
        return self._framerate

    def get_duration_ms(self):
        return self._duration_ms

# FIXME: add ffprobe? ffprobe -v quiet -print_format json -show_format -show_streams ${VIDEO}


class Metadata(object):
    """
    Instances of this class collect metadata of all the video tracks.
    """
    def __init__(self):
        """
        Create a mew Metadata instance.
        """
        self._video_tracks = []

    def _add_metadata(self, metadata):
        """
        Private method to add a new MetadataVideoTrack instance
        :param metadata: metadata of a video track
        """
        self._video_tracks.append(metadata)

    def get_videotracks(self):
        """
        Get metadata of all tracks
        :return: metadata of all tracks as a list
        """
        return self._video_tracks

    def _parse_dummy(self, filepath):
        """
        Private function to pretend to parse video at filepath, but don't do anything actually.
        :param filepath: path of video to parse as string
        """
        pass

    def _parse_kaa_metadata(self, filepath):
        """
        Private function to parse video at filepath, using kaa framework.
        :param filepath: path of video to parse as string
        """
        parseRes = kaa.metadata.parse(filepath)
        if not parseRes:
            return
        for video in parseRes.video:
            self._add_metadata(
                MetadataVideoTrack(
                    duration_ms=1000 * parseRes.length,
                    framerate=video.fps
                )
            )

    def _parse_pymediainfo(self, filepath):
        """
        Private function to parse video at filepath, using pymediainfo framework.
        :param filepath: path of video to parse as string
        """
        log.debug('pymediainfo: parsing "{filepath}" ...'.format(filepath=filepath))
        parseRes = pymediainfo.MediaInfo.parse(filepath)
        log.debug('... parsing FINISHED')
        for track in parseRes.tracks:
            log.debug('... found track type: "{track_type}"'.format(track_type=track.track_type))
            if track.track_type == 'Video':
                duration_ms = track.duration
                framerate = track.frame_rate
                log.debug('mode={}'.format(track.frame_rate_mode))
                if duration_ms is None or framerate is None:
                    log.debug('... Video track does not have duration and/or framerate.')
                    continue
                log.debug('... duration = {duration_ms} ms, framerate = {framerate} fps'.format(duration_ms=duration_ms,
                                                                                               framerate=framerate))
                self._add_metadata(
                    MetadataVideoTrack(
                        duration_ms=duration_ms,
                        framerate=float(framerate)
                    )
                )

parser = None

log.debug('Importing metadata parsing module ...')

if not parser:
    try:
        log.debug('Trying kaa.metadata ...')
        import kaa.metadata
        log.debug('... Succeeded')

        # Not interested in any output of the metadata package
        logging.getLogger('metadata').setLevel(logging.ERROR)

        log.debug('parsing module = kaa.metadata')
        parser = Metadata._parse_kaa_metadata
    except ImportError:
        log.debug('... Failed!')

if not parser:
    try:
        log.debug('Trying pymediainfo ...')
        import pymediainfo
        if pymediainfo.MediaInfo.can_parse:
            log.debug('... Succeeded')
            log.debug('parsing module = pymediainfo')
            parser = Metadata._parse_pymediainfo
        else:
            log.debug('... Failed!')
    except ImportError:
        log.debug('... Failed!')

if not parser:
    log.debug('parsing module = dummy parser')
    parser = Metadata._parse_dummy

Metadata.parse = parser

log.debug('... Importing metadata parsing module finished')

def parse(filepath):
    """
    Parse video at filepath
    :param filepath: path of video to parse as string
    :return: Metadata Instance of the video
    """
    metadata = Metadata()
    metadata.parse(filepath)
    return metadata
