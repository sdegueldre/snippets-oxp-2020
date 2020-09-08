odoo.define('custom_snippets.s_cart_products', function (require) {
'use strict';

const publicWidget = require('web.public.widget');
const DynamicSnippetCarousel = require('website.s_dynamic_snippet_carousel');

publicWidget.registry.dynamic_snippet_products = DynamicSnippetCarousel.extend({
    selector: '.s_cart_products',

    //--------------------------------------------------------------------------
    // Private
    //--------------------------------------------------------------------------

    /**
     * @override
     */
    _fetchData: async function () {
        const cards = await this._rpc({
            route: '/custom_snippets/cart_content',
        });
        this.data = [...$(cards)].filter(node => node.nodeType === 1).map(el => el.outerHTML);
    },
});
});
