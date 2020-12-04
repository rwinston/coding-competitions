let lines = document.body.innerText.split('\n');


let passports = []
let currentPassport = {}
for (let entry of lines) {
    console.log(entry);
    if (entry === "") { 
        passports.push(currentPassport); 
        currentPassport = {};
        continue;
    }
    entry.split(" ").forEach(function(x) { 
        let kv = x.split(":");
        currentPassport[kv[0]] = kv[1];
    });
}


let requiredFields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"];
let validation = {
    "byr" : function(x) { return parseInt(x)>=1920 && parseInt(x) <=2002},
    "iyr" : function(x) { return parseInt(x)>=2010 && parseInt(x) <=2020},
    "eyr" : function(x) { return parseInt(x)>=2020 && parseInt(x) <=2030},
    "hgt" : function(x) { 
        const re = /([0-9]+)(in|cm)/; 
        let m = x.match(re);
        if (m == null) return false;
        return (m[2] == "in" ? parseInt(m[1]) >= 59 && parseInt(m[1]) <= 76 : parseInt(m[1]) >= 150 && parseInt(m[1]) <= 193)
        },
    "hcl" : function(x) { return /^#[0-9a-f]{6}$/.test(x); },
    "ecl" : function(x) { return /^(amb|blu|gry|brn|grn|hzl|oth)$/.test(x); },
    "pid" : function(x) { return /^([0-9]{9})$/.test(x); },
    "cid" : function(x) { return true; }
};


let validPassports = 0;
for (let passport of passports) {
    // Part1 
    //if (requiredFields.every(prop => passport.hasOwnProperty(prop) && validation[prop](passport[prop]))) { validPassports++; }
    // Part2
    if (requiredFields.every(prop => passport.hasOwnProperty(prop) && validation[prop](passport[prop]))) { validPassports++; }

} 

console.log("Valid passports = " + validPassports);

