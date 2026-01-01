from genroutes import Route

def config_ios():
    pass

def config_junos(routes: list[Route]):
    config = []
    for route in routes:
        config.append(f"set routing-options static route {str(route.network)} as-path path \"{" ".join(route.aspath)}\"")
    
    return "\n".join(config)

platforms = {"ios": config_ios, "junos": config_junos}