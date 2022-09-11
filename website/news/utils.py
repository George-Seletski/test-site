class MyMixin(object):
    mixin_prop = ''
    
    def get_proper(self):
        return self.mixin_prop.upper()