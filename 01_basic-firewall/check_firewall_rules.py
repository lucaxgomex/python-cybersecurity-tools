def check_firewall_rules(rule_ip, rules):
    for x, y in rules.items():
        if rule_ip == x:
            return y
    return 'Allow'