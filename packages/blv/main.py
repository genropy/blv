#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='blv package',sqlschema='blv',sqlprefix=True,
                    name_short='Blv', name_long='Blv', name_full='Blv')
                    
    def config_db(self, pkg):
        pass
        
class Table(GnrDboTable):
    pass
