# -*- coding: utf-8 -*-

"""
spotifywebapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from spotifywebapi.api_helper import APIHelper


class Track1(object):

    """Implementation of the 'Track1' model.

    TODO: type model description here.

    Attributes:
        uri (str): Spotify URI

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uri": 'uri'
    }

    _optionals = [
        'uri',
    ]

    def __init__(self,
                 uri=APIHelper.SKIP):
        """Constructor for the Track1 class"""

        # Initialize members of the class
        if uri is not APIHelper.SKIP:
            self.uri = uri 

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
        uri = dictionary.get("uri") if dictionary.get("uri") else APIHelper.SKIP
        # Return an object of this model
        return cls(uri)
