/**
 * Execute a callback when all images have loaded.
 * needed because .load() doesn't work on cached images
 *
 * Usage:
 *   $('img.photo').imagesLoaded(myFunction)
 *     -> myFunction() { this == [jQuery collection of 'img'] }
 *
 *   $('img.photo').imagesLoaded(myFunction, myContext)
 *     -> myFunction() { this == myContext }
 *
 * Adds:
 *   + Image error counts as image load.
 *   + Empty 'img' set fires callback.
 *
 * MIT license. kottenator. 2011
 */

$.fn.imagesLoaded = function(callback, context) {
    var elems = this.filter('img'),
        len = elems.length,
        blank = "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///ywAAAAAAQABAAACAUwAOw==";

    context = context || elems;

    function countdown() {
        if (this.src != blank) {
            if (--len <= 0)
                callback.call(context, this);
        }
    }

    elems.each(function() {
        var src = this.src;
        this.src = blank;
        $(this).one('load error', countdown);
        this.src = src;
    });

    if (!elems.length)
        callback.call(context);

    return this;
};
