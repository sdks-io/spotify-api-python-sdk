# -*- coding: utf-8 -*-

"""
spotifywebapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from spotifywebapi.api_helper import APIHelper
from spotifywebapi.models.audiobook_object import AudiobookObject


class SavedAudiobookObject(object):

    """Implementation of the 'SavedAudiobookObject' model.

    TODO: type model description here.

    Attributes:
        added_at (datetime): The date and time the audiobook was saved
            Timestamps are returned in ISO 8601 format as Coordinated
            Universal Time (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ. If
            the time is imprecise (for example, the date/time of an album
            release), an additional field indicates the precision; see for
            example, release_date in an album object.
        audiobook (AudiobookObject): Information about the audiobook.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "added_at": 'added_at',
        "audiobook": 'audiobook'
    }

    _optionals = [
        'added_at',
        'audiobook',
    ]

    def __init__(self,
                 added_at=APIHelper.SKIP,
                 audiobook=APIHelper.SKIP):
        """Constructor for the SavedAudiobookObject class"""

        # Initialize members of the class
        if added_at is not APIHelper.SKIP:
            self.added_at = APIHelper.apply_datetime_converter(added_at, APIHelper.RFC3339DateTime) if added_at else None 
        if audiobook is not APIHelper.SKIP:
            self.audiobook = audiobook 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        added_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("added_at")).datetime if dictionary.get("added_at") else APIHelper.SKIP
        audiobook = AudiobookObject.from_dictionary(dictionary.get('audiobook')) if 'audiobook' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(added_at,
                   audiobook)
