# -*- coding: utf-8 -*-

"""
spotifywebapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from spotifywebapi.api_helper import APIHelper


class FollowersObject(object):

    """Implementation of the 'FollowersObject' model.

    TODO: type model description here.

    Attributes:
        href (str): This will always be set to null, as the Web API does not
            support it at the moment.
        total (int): The total number of followers.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "href": 'href',
        "total": 'total'
    }

    _optionals = [
        'href',
        'total',
    ]

    _nullables = [
        'href',
    ]

    def __init__(self,
                 href=APIHelper.SKIP,
                 total=APIHelper.SKIP):
        """Constructor for the FollowersObject class"""

        # Initialize members of the class
        if href is not APIHelper.SKIP:
            self.href = href 
        if total is not APIHelper.SKIP:
            self.total = total 

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
        href = dictionary.get("href") if "href" in dictionary.keys() else APIHelper.SKIP
        total = dictionary.get("total") if dictionary.get("total") else APIHelper.SKIP
        # Return an object of this model
        return cls(href,
                   total)
