from flaskapi import db, app

class Playlist(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    playlist = db.Column(db.String(), unique=True, nullable=False)

    def __repr__ (self):
        return f"Playlist: ({self.playlist})"

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


