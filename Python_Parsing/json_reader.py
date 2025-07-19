import json




def update_servers(config, updates):
    """
    Update the `origin_host` and `origin_port` of specified applications in the JSON dictionary.

    :param config: Dictionary containing application configurations.
    :param updates: Dictionary with app names as keys and the new `origin_host` and `origin_port` as values.
    :return: Updated configuration dictionary.
    """
    for app_name, server_details in updates.items():
        if app_name in config:
            if "servers" in config[app_name] and config[app_name]["servers"]:
                config[app_name]["servers"][0]["origin_host"] = server_details["origin_host"]
                config[app_name]["servers"][0]["origin_port"] = server_details["origin_port"]
    print(config)
    #return config

with open('appConfig.json') as file:
    data = json.load(file)


updates = {
    "jira": {"origin_host": "10.10.10.10", "origin_port": "8081"},
    "akamai-access-jenkins": {"origin_host": "1.1.1.1", "origin_port": "8919"},
    "ssh": {"origin_host": "0.1.1.1", "origin_port": "2222"},
}

update_servers(config=data, updates=updates)