# -*- coding: utf-8 -*-

"""
spotifywebapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from spotifywebapi.api_helper import APIHelper


class TrackRestrictionObject(object):

    """Implementation of the 'TrackRestrictionObject' model.

    TODO: type model description here.

    Attributes:
        reason (str): The reason for the restriction. Supported values: -
            `market` - The content item is not available in the given market.
            - `product` - The content item is not available for the user's
            subscription type. - `explicit` - The content item is explicit and
            the user's account is set to not play explicit content. 
            Additional reasons may be added in the future. **Note**: If you
            use this field, make sure that your application safely handles
            unknown values.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "reason": 'reason'
    }

    _optionals = [
        'reason',
    ]

    def __init__(self,
                 reason=APIHelper.SKIP):
        """Constructor for the TrackRestrictionObject class"""

        # Initialize members of the class
        if reason is not APIHelper.SKIP:
            self.reason = reason 

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
        reason = dictionary.get("reason") if dictionary.get("reason") else APIHelper.SKIP
        # Return an object of this model
        return cls(reason)
