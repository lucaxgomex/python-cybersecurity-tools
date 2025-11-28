import random
import generate_random_ip
import check_firewall_rules

def main():
    firewall_rules = {
        '192.168.1.1': 'block',
        '192.168.1.4': 'block',
        '192.168.1.9': 'block',
        '192.168.1.13': 'block',
        '192.168.1.16': 'block',
        '192.168.1.19': 'block',
    }

    for _ in range(12):
        ip_address = generate_random_ip.generate_random_ip()
        action = check_firewall_rules.check_firewall_rules(ip_address, firewall_rules)
        random_number = random.randint(0, 9999)

        print(f'IP Address: {ip_address}, Action: {action}, Random: {random_number}')

if __name__ == '__main__':
    main()