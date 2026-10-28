# 2nd Quarter Drill 2
from pyscript import display, document


def result_checker(e):
    document.getElementById('output').innerHTML = " "
    grade7 = {'Chester Roxas', 'Henri Fuentes', 'Justin Desquitado'}
    grade8 = {'Enami Asa', 'Hokazono Iroha', 'Nakamura Kazuha', 'Hwang Yeji'}
    grade9 = {'Victor Cortez', 'Stephen Smart', 'Kevin Larson'}
    grade10 = {'Joel Gonzales', 'Ezekiel Bacay', 'Dejan Laysa', 'Jaden Galvez'}

    first_name = document.getElementById('first_name').value
    last_name = document.getElementById('last_name').value
    new_members = first_name + " " + last_name
    new_members_set = {new_members}        
    all_members = grade7 | grade8 | grade9 | grade10 | new_members_set
    total_members = len(grade7 | grade8 | grade9 | grade10 | new_members_set)

    members_list = "<br>".join(sorted(all_members))

    document.getElementById('output').innerHTML = f'All members:<br>  {members_list}'
    display(f'Total members: {total_members}', target='output') 