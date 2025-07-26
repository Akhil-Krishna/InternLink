

from collections import namedtuple
from flask import Flask
from flask_bcrypt import Bcrypt

UserAccount = namedtuple('UserAccount', ['username', 'password'])

app = Flask(__name__)
flask_bcrypt = Bcrypt(app)

# Student accounts (20)
users = [
    UserAccount('sarah.chen', 'S@rahCh3n2025!'),
    UserAccount('james.wilson', 'J@mesW1ls0n#'),
    UserAccount('emily.martinez', 'Em1lyM@rt1nez$'),
    UserAccount('alex.thompson', 'Al3xTh0mps0n%'),
    UserAccount('priya.sharma', 'Pr1y@Sharm@1'),
    UserAccount('david.brown', 'D@v1dBr0wn^'),
    UserAccount('lisa.wang', 'L1s@W@ng*'),
    UserAccount('michael.jones', 'M1ch@elJ0nes&'),
    UserAccount('aisha.patel', 'A1sh@P@tel2025'),
    UserAccount('ryan.garcia', 'Ry@nG@rc1a!'),
    UserAccount('natalie.kim', 'N@t@l1eK1m#'),
    UserAccount('tom.anderson', 'T0mAnd3rs0n$'),
    UserAccount('sophia.rodriguez', 'S0ph1@R0dr1guez%'),
    UserAccount('ethan.lee', 'Eth@nL33^'),
    UserAccount('olivia.taylor', '0l1v1@T@yl0r*'),
    UserAccount('lucas.moore', 'Luc@sM00r3&'),
    UserAccount('isabella.clark', '1s@b3ll@Cl@rk!'),
    UserAccount('noah.walker', 'N0@hW@lk3r#'),
    UserAccount('zoe.allen', 'Z03@ll3n$'),
    UserAccount('jacob.hill', 'J@c0bH1ll%'),
    
    # Employer accounts (5)
    UserAccount('techcorp.hr', 'T3chC0rpHR2025!'),
    UserAccount('innovate.recruit', '1nn0v@t3R3crU1t#'),
    UserAccount('fintech.careers', 'F1nt3chC@r33rs$'),
    UserAccount('green.energy', 'Gr33nEn3rgy%'),
    UserAccount('media.creative', 'M3d1@Cr3@t1v3^'),
    
    # Admin accounts (2)
    UserAccount('admin.system', 'Adm1nSyst3m*'),
    UserAccount('admin.support', 'Adm1nSupp0rt&')
]

print('Username | Password | Hash | Password Matches Hash')
print('-' * 80)

for user in users:
    password_hash = flask_bcrypt.generate_password_hash(user.password)
    password_matches_hash = flask_bcrypt.check_password_hash(password_hash, user.password)
    print(f'{user.username} | {user.password} | {password_hash.decode()} | {password_matches_hash}')