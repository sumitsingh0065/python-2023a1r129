def check_quality(badge_string):
    special_chars = "@#$%"
    
    has_upper = any(c.isupper() for c in badge_string)
    has_lower = any(c.islower() for c in badge_string)
    has_digit = any(c.isdigit() for c in badge_string)
    has_special = any(c in special_chars for c in badge_string)
    
    if not (has_upper and has_lower and has_digit and has_special):
        return "NOT SECURE"
    
    for i in range(1, len(badge_string)):
        if badge_string[i] == badge_string[i-1]:
            return "NOT SECURE"
    
    digit_sum = sum(int(c) for c in badge_string if c.isdigit())
    if digit_sum % 2 != 0:
        return "NOT SECURE"
    
    return "SECURE"

# Example Input
result = check_quality("aB3@xY9#")
print(result)  # Output
