# -*- coding: utf-8 -*-

"""
spotifywebapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from spotifywebapi.api_helper import APIHelper
from spotifywebapi.models.explicit_content_settings_object import ExplicitContentSettingsObject
from spotifywebapi.models.external_url_object import ExternalUrlObject
from spotifywebapi.models.followers_object import FollowersObject
from spotifywebapi.models.image_object import ImageObject


class PrivateUserObject(object):

    """Implementation of the 'PrivateUserObject' model.

    TODO: type model description here.

    Attributes:
        country (str): The country of the user, as set in the user's account
            profile. An [ISO 3166-1 alpha-2 country
            code](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). _This
            field is only available when the current user has granted access
            to the
            [user-read-private](/documentation/web-api/concepts/scopes/#list-of
            -scopes) scope._
        display_name (str): The name displayed on the user's profile. `null`
            if not available.
        email (str): The user's email address, as entered by the user when
            creating their account. _**Important!** This email address is
            unverified; there is no proof that it actually belongs to the
            user._ _This field is only available when the current user has
            granted access to the
            [user-read-email](/documentation/web-api/concepts/scopes/#list-of-s
            copes) scope._
        explicit_content (ExplicitContentSettingsObject): The user's explicit
            content settings. _This field is only available when the current
            user has granted access to the
            [user-read-private](/documentation/web-api/concepts/scopes/#list-of
            -scopes) scope._
        external_urls (ExternalUrlObject): Known external URLs for this user.
        followers (FollowersObject): Information about the followers of the
            user.
        href (str): A link to the Web API endpoint for this user.
        id (str): The [Spotify user
            ID](/documentation/web-api/concepts/spotify-uris-ids) for the
            user.
        images (List[ImageObject]): The user's profile image.
        product (str): The user's Spotify subscription level: "premium",
            "free", etc. (The subscription level "open" can be considered the
            same as "free".) _This field is only available when the current
            user has granted access to the
            [user-read-private](/documentation/web-api/concepts/scopes/#list-of
            -scopes) scope._
        mtype (str): The object type: "user"
        uri (str): The [Spotify
            URI](/documentation/web-api/concepts/spotify-uris-ids) for the
            user.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "country": 'country',
        "display_name": 'display_name',
        "email": 'email',
        "explicit_content": 'explicit_content',
        "external_urls": 'external_urls',
        "followers": 'followers',
        "href": 'href',
        "id": 'id',
        "images": 'images',
        "product": 'product',
        "mtype": 'type',
        "uri": 'uri'
    }

    _optionals = [
        'country',
        'display_name',
        'email',
        'explicit_content',
        'external_urls',
        'followers',
        'href',
        'id',
        'images',
        'product',
        'mtype',
        'uri',
    ]

    def __init__(self,
                 country=APIHelper.SKIP,
                 display_name=APIHelper.SKIP,
                 email=APIHelper.SKIP,
                 explicit_content=APIHelper.SKIP,
                 external_urls=APIHelper.SKIP,
                 followers=APIHelper.SKIP,
                 href=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 images=APIHelper.SKIP,
                 product=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 uri=APIHelper.SKIP):
        """Constructor for the PrivateUserObject class"""

        # Initialize members of the class
        if country is not APIHelper.SKIP:
            self.country = country 
        if display_name is not APIHelper.SKIP:
            self.display_name = display_name 
        if email is not APIHelper.SKIP:
            self.email = email 
        if explicit_content is not APIHelper.SKIP:
            self.explicit_content = explicit_content 
        if external_urls is not APIHelper.SKIP:
            self.external_urls = external_urls 
        if followers is not APIHelper.SKIP:
            self.followers = followers 
        if href is not APIHelper.SKIP:
            self.href = href 
        if id is not APIHelper.SKIP:
            self.id = id 
        if images is not APIHelper.SKIP:
            self.images = images 
        if product is not APIHelper.SKIP:
            self.product = product 
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
        country = dictionary.get("country") if dictionary.get("country") else APIHelper.SKIP
        display_name = dictionary.get("display_name") if dictionary.get("display_name") else APIHelper.SKIP
        email = dictionary.get("email") if dictionary.get("email") else APIHelper.SKIP
        explicit_content = ExplicitContentSettingsObject.from_dictionary(dictionary.get('explicit_content')) if 'explicit_content' in dictionary.keys() else APIHelper.SKIP
        external_urls = ExternalUrlObject.from_dictionary(dictionary.get('external_urls')) if 'external_urls' in dictionary.keys() else APIHelper.SKIP
        followers = FollowersObject.from_dictionary(dictionary.get('followers')) if 'followers' in dictionary.keys() else APIHelper.SKIP
        href = dictionary.get("href") if dictionary.get("href") else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        images = None
        if dictionary.get('images') is not None:
            images = [ImageObject.from_dictionary(x) for x in dictionary.get('images')]
        else:
            images = APIHelper.SKIP
        product = dictionary.get("product") if dictionary.get("product") else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        uri = dictionary.get("uri") if dictionary.get("uri") else APIHelper.SKIP
        # Return an object of this model
        return cls(country,
                   display_name,
                   email,
                   explicit_content,
                   external_urls,
                   followers,
                   href,
                   id,
                   images,
                   product,
                   mtype,
                   uri)
