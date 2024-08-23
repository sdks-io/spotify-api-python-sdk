# -*- coding: utf-8 -*-

"""
spotifywebapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from spotifywebapi.api_helper import APIHelper
from spotifywebapi.models.cursor_object import CursorObject


class CursorPagingObject(object):

    """Implementation of the 'CursorPagingObject' model.

    TODO: type model description here.

    Attributes:
        href (str): A link to the Web API endpoint returning the full result
            of the request.
        limit (int): The maximum number of items in the response (as set in
            the query or by default).
        next (str): URL to the next page of items. ( `null` if none)
        cursors (CursorObject): The cursors used to find the next set of
            items.
        total (int): The total number of items available to return.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "href": 'href',
        "limit": 'limit',
        "next": 'next',
        "cursors": 'cursors',
        "total": 'total'
    }

    _optionals = [
        'href',
        'limit',
        'next',
        'cursors',
        'total',
    ]

    def __init__(self,
                 href=APIHelper.SKIP,
                 limit=APIHelper.SKIP,
                 next=APIHelper.SKIP,
                 cursors=APIHelper.SKIP,
                 total=APIHelper.SKIP):
        """Constructor for the CursorPagingObject class"""

        # Initialize members of the class
        if href is not APIHelper.SKIP:
            self.href = href 
        if limit is not APIHelper.SKIP:
            self.limit = limit 
        if next is not APIHelper.SKIP:
            self.next = next 
        if cursors is not APIHelper.SKIP:
            self.cursors = cursors 
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
        href = dictionary.get("href") if dictionary.get("href") else APIHelper.SKIP
        limit = dictionary.get("limit") if dictionary.get("limit") else APIHelper.SKIP
        next = dictionary.get("next") if dictionary.get("next") else APIHelper.SKIP
        cursors = CursorObject.from_dictionary(dictionary.get('cursors')) if 'cursors' in dictionary.keys() else APIHelper.SKIP
        total = dictionary.get("total") if dictionary.get("total") else APIHelper.SKIP
        # Return an object of this model
        return cls(href,
                   limit,
                   next,
                   cursors,
                   total)
