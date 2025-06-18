# med_script_email_list
Email Scraper tailored for FREIDA

Hi! 
This repo contains a script that will scrape emails for those looking for residencies or rotatations. 
The script is tailored to scrape the emails of openings listed on AMA's FRIEDA database. 

Here are the instructions: 
1. Go to: https://freida.ama-assn.org/
2. Search your respected specialties
3. apply respective filters for location
4. scroll to the bottom of the page and click "1" in the listing directory
   ![ok](https://github.com/user-attachments/assets/91a9e1da-4915-415b-81ca-0d8afe3517a9)
   
6. Once steps 1-3 have been completed copy the link in the browser but without the appended 1 (should be in this format: https://freida.ama-assn.org/search/list?spec=42736&fromHeader=true&page=)
8. open the script
9. in the function get_ids paste in the url that you had copied to the url variable *do not remove {page_num} (should be in this format:url = f'https://freida.ama-assn.org/search/list?spec=43236&loc=09&page={page_num}')
10. on line 79 replace the argument to the call get_ids(#) with the number page lists on from the website
    ![image](https://github.com/user-attachments/assets/01c2d261-ed9f-42ad-b58b-28734abc2880)
    in this case it should be  ids = get_ids(5)
11. run the script using /bin/python3 *path_of_script*/script.py   *replace with the path the script is located
12. the script will run and save an excel spread sheet of emails it has scraped in file called 'list.xlsx'
13. Enjoy

If you have any questions or need consultation feel free to email: eraadahmed13@gmail.com

