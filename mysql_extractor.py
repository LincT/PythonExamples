import MySQLdb  # python -m pip install <full path to the downloads folder>
from collections import namedtuple  # because I hate trying to guess data indexes in lists in tuples
import datetime


def unix_time_readable(unix_time: str)->datetime:
    time_format_string = '%Y-%m-%d'  # date as year month day
    conversion = datetime.datetime.fromtimestamp(int(unix_time)).strftime(time_format_string)
    return conversion


def main():

    conn = MySQLdb.Connect(
        "localhost",  # unless the database is on another machine this shouldn't need to be changed
        "",  # username to connect to the database
        "",  # password (super important, do not have this in code you post anywhere!!)
        ""  # database name (should match any use statement)
    )

    cur = conn.cursor()

    # query to gather everything from the stories table. can be refined if this uses too much ram to only select
    # necessary elements
    cur.execute("SELECT * from cms_stories")
    results = cur.fetchall()  # Fetch all the things in one dataset from previous query

    # the tuple format is just the column headers of the table without commas
    tuple_format = \
        "sid catid aid title time hometext bodytext comments counter topic informant notes ihome alanguage acomm " \
        "haspoll poll_id score ratings associated display_order"

    for each in results:  # basically for each row from the query
        item_tuple = namedtuple("story", tuple_format)
        story = item_tuple._make(each)  # using make allows us to map the output to the named columns
        time = unix_time_readable(story.time)

        # in my project directory I have the code in a sub folder, so I backup one level, then nav to the other
        # directory of \docs (yes i'm on windows, if you're running this in mac/linux let me know what bugs you get)
        base_dir = "..\\docs\\"
        file_name = " - ".join([time, story.informant, story.title])  # example filename generator
        file_text = "\n".join([story.title, story.informant, time, story.hometext, story.bodytext])

        # file handling, this will overwrite existing files on rerun
        with open(base_dir+file_name+".txt", 'w') as file:
            file.write(str(file_text))


main()
