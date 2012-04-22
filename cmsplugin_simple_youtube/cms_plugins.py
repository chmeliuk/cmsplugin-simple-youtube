from django.utils.translation import ugettext as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import SimpleYoutubePointer

class SimpleYouTubePlugin(CMSPluginBase):
    model = SimpleYoutubePointer
    name = _("Simple: YouTube")
    render_template = "cmsplugin_simple_youtube/fancy_iframe.html"
    text_enabled = True

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance.youtube,
            'placeholder': placeholder
        })
        return context

    def icon_src(self, instance):
        return u'http://i4.ytimg.com/vi/%s/default.jpg' % instance.youtube.video_id

plugin_pool.register_plugin(SimpleYouTubePlugin)
