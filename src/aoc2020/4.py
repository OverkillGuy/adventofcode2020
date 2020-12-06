import re


def day4_validate(passport_pairs):
    """
    >>> day4_validate([("ecl","gry"), ("pid","860033327"), ("eyr","2020"),("hcl","#fffffd"),("byr","1937"), ("iyr","2017"), ("cid","147"),("hgt","183cm")])
    True
    >>> day4_validate([("iyr","2013"),("ecl","amb"),("cid","350"),("eyr","2023"),("pid","028048884"),("hcl","#cfa07d"),("byr","1929")])
    False
    >>> day4_validate([("hcl","#ae17e1"),("iyr","2013"),("eyr","2024"),("ecl","brn"),("pid","760753108"),("byr","1931"),("hgt","179cm")])
    True
    >>> day4_validate([("hcl","#cfa07d"),("eyr","2025"),("pid","166559648"),("iyr","2011"),("ecl","brn"),("hgt","59in")])
    False
    """
    d = dict()
    for k, v in passport_pairs:
        d[k] = v
    required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for key in required_keys:
        if key not in d:
            return False
    return True


def day4_1(text):
    """
    >>> day4_1("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\\nbyr:1937 iyr:2017 cid:147 hgt:183cm\\n\\niyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\\nhcl:#cfa07d byr:1929\\n\\nhcl:#ae17e1 iyr:2013\\neyr:2024\\necl:brn pid:760753108 byr:1931\\nhgt:179cm\\n\\nhcl:#cfa07d eyr:2025 pid:166559648\\niyr:2011 ecl:brn hgt:59in")
    2
    """
    entries = [entry.replace("\n", " ") for entry in text.split("\n\n")]
    regex = re.compile("([a-z]+:[#a-z0-9]+)+")
    acc = 0
    for entry in entries:
        fields = re.findall(regex, entry)
        kv_pairs = [i.split(":") for i in fields]
        if day4_validate(kv_pairs):
            acc += 1
    return acc


def day4_2(text):
    """
    >>> day4_2("eyr:1972 cid:100\\nhcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926\\n\\niyr:2019\\nhcl:#602927 eyr:1967 hgt:170cm\\necl:grn pid:012533040 byr:1946\\n\\nhcl:dab227 iyr:2012\\necl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277\\n\\nhgt:59cm ecl:zzz\\neyr:2038 hcl:74454a iyr:2023\\npid:3556412378 byr:2007\\n\\npid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980\\nhcl:#623a2f\\n\\neyr:2029 ecl:blu cid:129 byr:1989\\niyr:2014 pid:896056539 hcl:#a97842 hgt:165cm\\n\\nhcl:#888785\\nhgt:164cm byr:2001 iyr:2015 cid:88\\npid:545766238 ecl:hzl\\neyr:2022\\n\\niyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719\\n")
    4
    """
    entries = [entry.replace("\n", " ") for entry in text.split("\n\n")]
    regex = re.compile("([a-z]+:[#a-z0-9]+)+")
    acc = 0
    for entry in entries:
        fields = re.findall(regex, entry)
        kv_pairs = [i.split(":") for i in fields]
        d = dict()
        for k, v in kv_pairs:
            d[k] = v
        if day4_validator2(d):
            acc += 1
    return acc


# TODO: Replace this with all(rule(d) for rule in rules)
def day4_validator2(passport_pairs):
    rules = [
        rule_keys,
        rule_byr,
        rule_eyr,
        rule_iyr,
        rule_hgt,
        rule_hcl,
        rule_ecl,
        rule_pid,
    ]
    for validation_rule in rules:
        if not validation_rule(passport_pairs):
            return False
    return True


def rule_keys(d):
    required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for key in required_keys:
        if key not in d:
            return False
    return True


def rule_byr(d):
    """
    >>> rule_byr({"byr": "2002"})
    True
    >>> rule_byr({"byr": "2003"})
    False
    """
    return (len(d["byr"]) == 4) and (1920 <= int(d["byr"]) <= 2002)


def rule_iyr(d):
    return (len(d["iyr"]) == 4) and (2010 <= int(d["iyr"]) <= 2020)


def rule_eyr(d):
    return (len(d["eyr"]) == 4) and (2020 <= int(d["eyr"]) <= 2030)


def rule_hgt(d):
    """
    >>> rule_hgt({"hgt": "60in"})
    True
    >>> rule_hgt({"hgt": "190cm"})
    True
    >>> rule_hgt({"hgt": "190in"})
    False
    >>> rule_hgt({"hgt": "190"})
    False
    """
    hgt = d["hgt"]
    unit = hgt[-2:]
    if unit not in ["cm", "in"]:
        return False
    value = int(hgt[:-2])
    if unit == "cm":
        return 150 <= value <= 193
    else:
        return 59 <= value <= 76


def rule_hcl(d):
    """
    >>> rule_hcl({"hcl": "#123abc"})
    True
    >>> rule_hcl({"hcl": "#123abz"})
    False
    >>> rule_hcl({"hcl": "123abc"})
    False
    """
    hcl = d["hcl"]
    if hcl[0] != "#":
        return False
    color = hcl[1:]
    if len(color) != 6:
        return False
    for char in color:
        if char not in "0123456789abcdef":
            return False
    return True


def rule_ecl(d):
    """
    >>> rule_ecl({"ecl": "brn"})
    True
    >>> rule_ecl({"ecl": "wat"})
    False
    """
    return d["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def rule_pid(d):
    """
    >>> rule_pid({"pid": "000000001"})
    True
    >>> rule_pid({"pid": "0123456789"})
    False
    """
    return len(d["pid"]) == 9


if __name__ == "__main__":
    with open("input4.txt", "r") as fd:
        data = fd.read()
    print(day4_1(data))
    print(day4_2(data))
