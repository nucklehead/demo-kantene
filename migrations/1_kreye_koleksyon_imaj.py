from mongodb_migrations.base import BaseMigration


class Migration(BaseMigration):
    def upgrade(self):
        self.db.create_collection('imaj_slack')

    def downgrade(self):
        self.db['imaj_slack'].drop()
