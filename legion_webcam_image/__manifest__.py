# -*- coding: utf-8 -*-
{
    "name": "Live WebCam Image | Image Widget",
    "version": "15.0.1.0",

    "author": "Bytelegion",
    "website": "http://www.bytelegions.com",
    'company': 'Bytelegion',

    "depends": ["web"],
    "license": "LGPL-3",
    "category": "web",

    "summary": """Allows to take image with WebCam[TAGS], web camera, web photo, web images, camera image,
     snapshot web, snapshot webcam, snapshot picture, web contact image,
     web product image, online mobile web image and product image.""",

    "depends": [
        "web",
    ],

    'assets': {
        'web.assets_backend': [
            'legion_webcam_image/static/src/**/*.css',
            'legion_webcam_image/static/src/js/webcam_widget_new.js',
        ],
        'web.assets_qweb': [
            'legion_webcam_image/static/src/xml/web_widget_image_webcam.xml',
        ],
    },
    "installable": True,
    
    'images': ['static/description/banner.gif'],
    
}
