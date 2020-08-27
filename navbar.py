import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("home", href='/')),
        dbc.NavItem(dbc.NavLink("Page 1", href='/page-1')),
        dbc.NavItem(dbc.NavLink("Page 2", href='/page-2')),
    ],
    brand="NavbarSimple",
    brand_href="/",
    color="primary",
    dark=True,
)
