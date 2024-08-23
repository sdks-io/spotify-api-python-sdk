# -*- coding: utf-8 -*-

"""
spotifywebapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from spotifywebapi.models.track_object import TrackObject


class PagingTrackObject(object):

    """Implementation of the 'PagingTrackObject' model.

    TODO: type model description here.

    Attributes:
        href (str): A link to the Web API endpoint returning the full result
            of the request
        limit (int): The maximum number of items in the response (as set in
            the query or by default).
        next (str): URL to the next page of items. ( `null` if none)
        offset (int): The offset of the items returned (as set in the query or
            by default)
        previous (str): URL to the previous page of items. ( `null` if none)
        total (int): The total number of items available to return.
        items (List[TrackObject]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "href": 'href',
        "limit": 'limit',
        "next": 'next',
        "offset": 'offset',
        "previous": 'previous',
        "total": 'total',
        "items": 'items'
    }

    _nullables = [
        'next',
        'previous',
    ]

    def __init__(self,
                 href=None,
                 limit=None,
                 next=None,
                 offset=None,
                 previous=None,
                 total=None,
                 items=None):
        """Constructor for the PagingTrackObject class"""

        # Initialize members of the class
        self.href = href 
        self.limit = limit 
        self.next = next 
        self.offset = offset 
        self.previous = previous 
        self.total = total 
        self.items = items 

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
        href = dictionary.get("href") if dictionary.get("href") else None
        limit = dictionary.get("limit") if dictionary.get("limit") else None
        next = dictionary.get("next") if dictionary.get("next") else None
        offset = dictionary.get("offset") if dictionary.get("offset") else None
        previous = dictionary.get("previous") if dictionary.get("previous") else None
        total = dictionary.get("total") if dictionary.get("total") else None
        items = None
        if dictionary.get('items') is not None:
            items = [TrackObject.from_dictionary(x) for x in dictionary.get('items')]
        # Return an object of this model
        return cls(href,
                   limit,
                   next,
                   offset,
                   previous,
                   total,
                   items)
