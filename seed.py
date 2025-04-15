import csv
import random
from app import app, db
from models import Episode, Guest, Appearance

def seed_data():
    with app.app_context():
        # Clear existing data
        db.session.query(Appearance).delete()
        db.session.query(Episode).delete()
        db.session.query(Guest).delete()
        db.session.commit()

        guests_dict = {}

        with open('seed.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            episode_counter = 1
            for row in reader:
                # Create guest if not already created
                raw_guest_list = row['Raw_Guest_List'].strip()
                occupation = row['GoogleKnowlege_Occupation'].strip() or "Unknown"

                if raw_guest_list not in guests_dict:
                    guest = Guest(name=raw_guest_list, occupation=occupation)
                    db.session.add(guest)
                    guests_dict[raw_guest_list] = guest
                else:
                    guest = guests_dict[raw_guest_list]

                # Create episode
                episode = Episode(date=row['YEAR'], number=episode_counter)
                db.session.add(episode)

                db.session.flush()  # To get IDs before commit

                # Create appearance with random rating
                appearance = Appearance(
                    rating=random.randint(1, 5),
                    episode_id=episode.id,
                    guest_id=guest.id
                )
                db.session.add(appearance)

                episode_counter += 1

        db.session.commit()
        print("Database seeded successfully.")

if __name__ == '__main__':
    seed_data()