# -*- coding: utf-8 -*-

"""
spotifywebapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from spotifywebapi.api_helper import APIHelper
from spotifywebapi.models.external_url_object import ExternalUrlObject
from spotifywebapi.models.followers_object import FollowersObject
from spotifywebapi.models.image_object import ImageObject


class ArtistObject(object):

    """Implementation of the 'ArtistObject' model.

    TODO: type model description here.

    Attributes:
        external_urls (ExternalUrlObject): Known external URLs for this
            artist.
        followers (FollowersObject): Information about the followers of the
            artist.
        genres (List[str]): A list of the genres the artist is associated
            with. If not yet classified, the array is empty.
        href (str): A link to the Web API endpoint providing full details of
            the artist.
        id (str): The [Spotify
            ID](/documentation/web-api/concepts/spotify-uris-ids) for the
            artist.
        images (List[ImageObject]): Images of the artist in various sizes,
            widest first.
        name (str): The name of the artist.
        popularity (int): The popularity of the artist. The value will be
            between 0 and 100, with 100 being the most popular. The artist's
            popularity is calculated from the popularity of all the artist's
            tracks.
        mtype (TypeEnum): The object type.
        uri (str): The [Spotify
            URI](/documentation/web-api/concepts/spotify-uris-ids) for the
            artist.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "external_urls": 'external_urls',
        "followers": 'followers',
        "genres": 'genres',
        "href": 'href',
        "id": 'id',
        "images": 'images',
        "name": 'name',
        "popularity": 'popularity',
        "mtype": 'type',
        "uri": 'uri'
    }

    _optionals = [
        'external_urls',
        'followers',
        'genres',
        'href',
        'id',
        'images',
        'name',
        'popularity',
        'mtype',
        'uri',
    ]

    def __init__(self,
                 external_urls=APIHelper.SKIP,
                 followers=APIHelper.SKIP,
                 genres=APIHelper.SKIP,
                 href=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 images=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 popularity=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 uri=APIHelper.SKIP):
        """Constructor for the ArtistObject class"""

        # Initialize members of the class
        if external_urls is not APIHelper.SKIP:
            self.external_urls = external_urls 
        if followers is not APIHelper.SKIP:
            self.followers = followers 
        if genres is not APIHelper.SKIP:
            self.genres = genres 
        if href is not APIHelper.SKIP:
            self.href = href 
        if id is not APIHelper.SKIP:
            self.id = id 
        if images is not APIHelper.SKIP:
            self.images = images 
        if name is not APIHelper.SKIP:
            self.name = name 
        if popularity is not APIHelper.SKIP:
            self.popularity = popularity 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
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
        external_urls = ExternalUrlObject.from_dictionary(dictionary.get('external_urls')) if 'external_urls' in dictionary.keys() else APIHelper.SKIP
        followers = FollowersObject.from_dictionary(dictionary.get('followers')) if 'followers' in dictionary.keys() else APIHelper.SKIP
        genres = dictionary.get("genres") if dictionary.get("genres") else APIHelper.SKIP
        href = dictionary.get("href") if dictionary.get("href") else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        images = None
        if dictionary.get('images') is not None:
            images = [ImageObject.from_dictionary(x) for x in dictionary.get('images')]
        else:
            images = APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        popularity = dictionary.get("popularity") if dictionary.get("popularity") else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        uri = dictionary.get("uri") if dictionary.get("uri") else APIHelper.SKIP
        # Return an object of this model
        return cls(external_urls,
                   followers,
                   genres,
                   href,
                   id,
                   images,
                   name,
                   popularity,
                   mtype,
                   uri)
