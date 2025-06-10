import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import re
import pandas as pd

def get_ids(num_pages):
    id_list = []
    for num in range(num_pages):
        page_num = num + 1
        url = f'https://freida.ama-assn.org/search/list?spec=43236&loc=09&page={page_num}' #replace with url of choice
        session = HTMLSession()
        response = session.get(url)
        response.html.render(sleep=5)
        soup = BeautifulSoup(response.html.html, 'html.parser')

        schools =  soup.find_all('footer', class_ = 'search-result-card__footer')
        session.close()
        id_pattern = r'\d{10}'
        
        for school in schools:
            school_text = school.get_text(separator=' ', strip=True)
            found_id = re.findall(id_pattern, school_text)
            id_list.extend(found_id)
        
    return id_list

def school_listing(id):
    url = f'https://freida.ama-assn.org/program/{id}/overview'
    session = HTMLSession()
    response = session.get(url)
    response.html.render(sleep = 2)
    soup = BeautifulSoup(response.html.html, 'html.parser')


    schools = soup.find_all('div', class_ = 'details__title')
    school_pattern = r'.*Program$'
    school_text = schools[0].get_text(separator=' ', strip=True)
    match = re.search(school_pattern, school_text)
    school_name = match.group() if match else "N/A"

    loc_pattern = r'.*,\s[A-Z]{2}$'
    locations = soup.find_all('div', class_ = 'details__bottom-line__location ng-star-inserted')
    location = locations[0].get_text(separator=' ', strip=True)
    contacts = soup.find_all('small', class_ = 'contact-info__contacts__details')

    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    email_list = []
    session.close()
    for contact in contacts:
        contact_text = contact.get_text(separator=' ', strip=True)
        found_emails = re.findall(email_pattern, contact_text)
        email_list.extend(found_emails)
    if len(email_list) >= 2:
        program_data = {
            "Program Name": school_name,
            "Location": location,
            "Program Director Email": email_list[0],
            "Contact Person Email": email_list[1]
        }
    elif len(email_list) == 1:
        program_data = {
            "Program Name": school_name,
            "Location": location,
            "Program Director Email": "N/A",
            "Contact Person Email": email_list[0]
        }
    else:
        program_data = {
            "Program Name": school_name,
            "Location": location,
            "Program Director Email": "N/A",
            "Contact Person Email": "N/A"
        }
    print(program_data)
    return program_data

program_data = []
ids = get_ids(2)
for id in ids:
    corr_program = school_listing(id)
    program_data.append(corr_program)

df = pd.DataFrame(program_data)

# Save to Excel
excel_file_path = 'list.xlsx'
df.to_excel(excel_file_path, index=False)

print(f"\nEmails extracted and saved to {excel_file_path}")

# Close the HTMLSession when done
