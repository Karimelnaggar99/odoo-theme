{
    "name": "Clarity Backend Theme for community",
    "version": "16.0.1.0.0",
    'author': "Terabits Technolab",
    'summary': """   
        Clarity backend theme   
        Odoo Backend Theme, Odoo Community Backend Theme, Web backend Theme, Web Responsive Odoo Theme, New theme design, New design, Multi Level Menu,
        Web Responsive Odoo Backend Theme, Odoo Theme, Odoo Modern Theme, Odoo Modern Backend Theme Odoo, Advance Theme Backend Advanced, Sidebar Light,
        All in one, New advanced Odoo Menu, Sidebar apps, New design, Left sidebar menu, Web menu, Odoo backend menu, Web Responsive menu, Sidebar White,
        Advance Menu Odoo App Menu Apps, Advanced Apps Menu, Elegant Menu, Menuitem, Web App Menu Backend, Menu Odoo Backend, Collapse Menu, Light Sidebar,
        Expand Menu, Collapsed Menu, Expanded Menu, New Style Menus, Advanced Sidebar Menu, Advance Sidebar Menu, Responsive Menu Sidebar, Sidebar Theme,
        Responsive Sidebar, Hide menu, Show Menu, Hide Sidebar, Show Sidebar, Toggle Menu, Toggle Sidebar, All in one Dynamic Menu Access, Menu Theme,
        Visibility Menu Visibility, Quick Backend Menu, Dropdown Menu, Parent Menus, Shortcut Menus Shortcut, Menu Icons, Collapsible menu Odoo,
        Customize Menu Customize Sidebar App, Customization Menu Customization App Sidebar Customization Sidebar Apps, Group Left Menu in Odoo,
        Global Search Menu Search, Global Menu Access Global Apps Menu Global, Group Top Menu in Odoo, Odoo Foldable Menu Applications, Navbar,
        App web Menu, Quick Menu Access Menu, Menu Dynamic Sidebar, Any menu, Easy Access for menuitems, User Menu Users, All in one Sidebar,
        Advanced Menu, Advanced Odoo Menu Backend Odoo Web Theme Web Odoo, Elegant Theme Simple Theme, Advance List View Manager, Menu Style,
        Advanced List View Advanced Pivot View Theme Table View Theme Form View Theme Advanced Forms, Beautiful Theme Design, New Style Theme
    
        The ultimate Odoo Backend theme with the most advanced key features of all time. Get your own personalized view while working on the Backend system with a wide range of choices. Spiffy theme has 3 in 1 Theme Style, Progressive Web App, Fully Responsive for all apps, Configurable Apps Icon, App Drawer with global search, RTL & Multi-Language Support, and many other key features.  

        Ditch the boring theme while working; opt for the Odoo Arc Backend Theme and increase your business performance.
        Switch from Light and Dark mode as per your working necessities. Arc Backend Theme, Backend Theme, Responsive Theme, 
        Fully Functional Theme, Flexible Backend Theme, Fast Backend Theme, Modern Multipurpose Theme, Lightweight Backend Theme, 
        Animated Backend Theme, Advance Material Backend Theme, Customizable Backend Theme, Multi Tab Backend Theme Odoo, 
        Attractive Theme for Backend, Elegant Backend Theme, Community Backend Theme, Odoo Community Backend Theme, 
        Fully Functional Backend Theme, Responsive Web Client, Mobile Theme, Backend UI, Mobile Interface,
        Mobile Responsive for Odoo Community, Dual Color Backend Theme, Flexible Enterprise Theme, Enterprise Backend Theme
    """,
    'description': """ 
        Clarity backend theme   
        Odoo Backend Theme, Odoo Community Backend Theme, Web backend Theme, Web Responsive Odoo Theme, New theme design, New design, Multi Level Menu,
        Web Responsive Odoo Backend Theme, Odoo Theme, Odoo Modern Theme, Odoo Modern Backend Theme Odoo, Advance Theme Backend Advanced, Sidebar Light,
        All in one, New advanced Odoo Menu, Sidebar apps, New design, Left sidebar menu, Web menu, Odoo backend menu, Web Responsive menu, Sidebar White,
        Advance Menu Odoo App Menu Apps, Advanced Apps Menu, Elegant Menu, Menuitem, Web App Menu Backend, Menu Odoo Backend, Collapse Menu, Light Sidebar,
        Expand Menu, Collapsed Menu, Expanded Menu, New Style Menus, Advanced Sidebar Menu, Advance Sidebar Menu, Responsive Menu Sidebar, Sidebar Theme,
        Responsive Sidebar, Hide menu, Show Menu, Hide Sidebar, Show Sidebar, Toggle Menu, Toggle Sidebar, All in one Dynamic Menu Access, Menu Theme,
        Visibility Menu Visibility, Quick Backend Menu, Dropdown Menu, Parent Menus, Shortcut Menus Shortcut, Menu Icons, Collapsible menu Odoo,
        Customize Menu Customize Sidebar App, Customization Menu Customization App Sidebar Customization Sidebar Apps, Group Left Menu in Odoo,
        Global Search Menu Search, Global Menu Access Global Apps Menu Global, Group Top Menu in Odoo, Odoo Foldable Menu Applications, Navbar,
        App web Menu, Quick Menu Access Menu, Menu Dynamic Sidebar, Any menu, Easy Access for menuitems, User Menu Users, All in one Sidebar,
        Advanced Menu, Advanced Odoo Menu Backend Odoo Web Theme Web Odoo, Elegant Theme Simple Theme, Advance List View Manager, Menu Style,
        Advanced List View Advanced Pivot View Theme Table View Theme Form View Theme Advanced Forms, Beautiful Theme Design, New Style Theme
    
        The ultimate Odoo Backend theme with the most advanced key features of all time. Get your own personalized view while working on the Backend system with a wide range of choices. Spiffy theme has 3 in 1 Theme Style, Progressive Web App, Fully Responsive for all apps, Configurable Apps Icon, App Drawer with global search, RTL & Multi-Language Support, and many other key features.  

        Ditch the boring theme while working; opt for the Odoo Arc Backend Theme and increase your business performance.
        Switch from Light and Dark mode as per your working necessities. Arc Backend Theme, Backend Theme, Responsive Theme, 
        Fully Functional Theme, Flexible Backend Theme, Fast Backend Theme, Modern Multipurpose Theme, Lightweight Backend Theme, 
        Animated Backend Theme, Advance Material Backend Theme, Customizable Backend Theme, Multi Tab Backend Theme Odoo, 
        Attractive Theme for Backend, Elegant Backend Theme, Community Backend Theme, Odoo Community Backend Theme, 
        Fully Functional Backend Theme, Responsive Web Client, Mobile Theme, Backend UI, Mobile Interface,
        Mobile Responsive for Odoo Community, Dual Color Backend Theme, Flexible Enterprise Theme, Enterprise Backend Theme
    """,
    "sequence": 7,
    "license": "OPL-1",
    "category": "Themes/Backend",
    "website": "https://www.terabits.xyz",
    "depends": ["web","base_setup"],
    "data": [
        'views/res_config_setting.xml',
        'views/res_users.xml',
        'views/webclient_templates.xml'
    ],
    "assets": {
        "web.assets_frontend": [
            'clarity_backend_theme_bits/static/src/scss/login.scss'
        ],
        "web.assets_backend": [   
            'clarity_backend_theme_bits/static/src/xml/WebClient.xml',
            'clarity_backend_theme_bits/static/src/xml/navbar/sidebar.xml',
            'clarity_backend_theme_bits/static/src/xml/systray_items/SidebarBottom.xml',
            'clarity_backend_theme_bits/static/src/js/SidebarBottom.js',
            'clarity_backend_theme_bits/static/src/xml/systray_items/user_menu.xml',  
            'clarity_backend_theme_bits/static/src/js/WebClient.js',
            'clarity_backend_theme_bits/static/src/scss/layout.scss',
            'clarity_backend_theme_bits/static/src/scss/navbar.scss',
            'clarity_backend_theme_bits/static/src/js/navbar.js',
        ],
    }, 
    'installable': True,
    'application': True,
    'auto_install': False,  
    'images': [
        'static/description/logo.gif',
        'static/description/theme_screenshot.gif',
    ],
}
