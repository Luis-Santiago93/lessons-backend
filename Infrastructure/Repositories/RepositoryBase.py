class RepositoryBase(object):
    entityBase = None
    entityName = None

    def __init__(self, db, EntityBase, EntityName):
        self.db = db
        self.entityBase = EntityBase
        self.entityName = EntityName

    def session(self):
        return self.db.session

    def get_all(self):
        try:
            return self.session().query(self.entityBase).filter_by(IsVigente = True).all()
            self.session().commit()
        except Exception as e:
            return None
            self.session().rollback()
            raise
        finally:
            self.session().close()

    def get_by_id(self, item):
        try:
            return self.session().query(self.entityBase).filter_by(IsVigente = True).one()
            self.session().commit()
        except Exception as e:
            return None
            self.session().rollback()
            raise
        finally:
            self.session().close()

    def insert(self, item):
        try:    
            self.session().add(item)
            self.session().commit()
            self.session().refresh(item)
            return item
        except Exception as e:
            self.session().rollback()
            raise
        finally:
            self.session().close()

    def delete(self, id):
        try:
            i = self.session().query(self.entityBase).get(id)
            self.session().delete(i)
            self.session().commit()
            return i
        except Exception as e:
            self.session().rollback()
            raise
        finally:
            self.session().close()

    def update(self, item, id):
        try:
            i = self.session().query(self.entityBase).get(id)
            for key, value in sorted(item.items()):
                setattr(i, key, value)
            self.session().commit()
            return item
        except Exception as e:
            self.session().rollback()
            raise
        finally:
            self.session().close()
            
    
