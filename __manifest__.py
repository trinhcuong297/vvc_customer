# -*- encoding: utf-8 -*-
##############################################################################
#
#    Odoo, Customer Service System
#    Copyright (C) 2023 VVC Green - VVC Tech (<https://www.vvc.com.vn>). All Rights Reserved
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Customer Service System",
    "version": "15.0.1.0.0",
    "sequence": -100,
    "category": "Tools",
    "summary": "Customer Service System",
    "author": "VVC Tech",
    "license": 'AGPL-3',
    "website": 'https://www.vvc.com.vn',
    "description": """
This module is linked with VVC Green app!
    """,
    "depends": [],
    "data": [
        "security\ir.model.access.csv",
        "views/menu.xml"
    ],
    'assets': {},
    "test": [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
