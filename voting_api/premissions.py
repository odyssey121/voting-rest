from rest_framework import permissions


class AnswerEditingPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, answer):
        if request.user:
            return request.user == answer.user
        return False