# from base import db
# from base.com.vo.login_vo import (LoginVO)

from base import db


class LoginDAO:
    def insert_user(self,login_vo):
        db.session.add(login_vo)
        db.session.commit()

    def get_user_by_username(self, username):
        return LoginVO.query.filter_by(username=username).first()

    # def view_category(self):
    #     category_vo_list = LoginVO.query.all()
    #     return category_vo_list
    #
    # def delete_category(self,category_vo):
    #     category_vo_list=LoginVO.query.get(category_vo.category_id)
    #     db.session.delete(category_vo_list)
    #     db.session.commit()
    #
    # def edit_category(self,category_vo):
    #     category_vo_list=LoginVO.query.filter_by(category_id=category_vo.category_id).all()
    #     return category_vo_list
    #
    # def update_category(self,category_vo):
    #     db.session.merge(category_vo)
    #     db.session.commit()