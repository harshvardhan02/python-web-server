from flask import Blueprint, render_template

breadcrumb = Blueprint('breadcrumb', __name__)

@breadcrumb.app_template_filter('breadcrumbs')
def render_breadcrumbs(items):
    return render_template('breadcrumbs.html', items=items)