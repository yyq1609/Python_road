from django import forms
from django.utils.safestring import mark_safe

from rbac import models


class BsModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BsModelForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, forms.RadioSelect):
                continue
            field.widget.attrs['class'] = 'form-control'


data = [['fa-address-book', '<i aria-hidden="true" class="fa fa-address-book"></i>'],
        ['fa-address-book-o', '<i aria-hidden="true" class="fa fa-address-book-o"></i>'],
        ['fa-address-card', '<i aria-hidden="true" class="fa fa-address-card"></i>'],
        ['fa-address-card-o', '<i aria-hidden="true" class="fa fa-address-card-o"></i>'],
        ['fa-adjust', '<i aria-hidden="true" class="fa fa-adjust"></i>'],
        ['fa-american-sign-language-interpreting',
         '<i aria-hidden="true" class="fa fa-american-sign-language-interpreting"></i>'],
        ['fa-anchor', '<i aria-hidden="true" class="fa fa-anchor"></i>'],
        ['fa-archive', '<i aria-hidden="true" class="fa fa-archive"></i>'],
        ['fa-area-chart', '<i aria-hidden="true" class="fa fa-area-chart"></i>'],
        ['fa-arrows', '<i aria-hidden="true" class="fa fa-arrows"></i>'],
        ['fa-arrows-h', '<i aria-hidden="true" class="fa fa-arrows-h"></i>'],
        ['fa-arrows-v', '<i aria-hidden="true" class="fa fa-arrows-v"></i>'],
        ['fa-asl-interpreting', '<i aria-hidden="true" class="fa fa-asl-interpreting"></i>'],
        ['fa-assistive-listening-systems',
         '<i aria-hidden="true" class="fa fa-assistive-listening-systems"></i>'],
        ['fa-asterisk', '<i aria-hidden="true" class="fa fa-asterisk"></i>'],
        ['fa-at', '<i aria-hidden="true" class="fa fa-at"></i>'],
        ['fa-audio-description', '<i aria-hidden="true" class="fa fa-audio-description"></i>'],
        ['fa-automobile', '<i aria-hidden="true" class="fa fa-automobile"></i>'],
        ['fa-balance-scale', '<i aria-hidden="true" class="fa fa-balance-scale"></i>'],
        ['fa-ban', '<i aria-hidden="true" class="fa fa-ban"></i>'],
        ['fa-bank', '<i aria-hidden="true" class="fa fa-bank"></i>'],
        ['fa-bar-chart', '<i aria-hidden="true" class="fa fa-bar-chart"></i>'],
        ['fa-bar-chart-o', '<i aria-hidden="true" class="fa fa-bar-chart-o"></i>'],
        ['fa-barcode', '<i aria-hidden="true" class="fa fa-barcode"></i>'],
        ['fa-bars', '<i aria-hidden="true" class="fa fa-bars"></i>'],
        ['fa-bath', '<i aria-hidden="true" class="fa fa-bath"></i>'],
        ['fa-bathtub', '<i aria-hidden="true" class="fa fa-bathtub"></i>'],
        ['fa-battery', '<i aria-hidden="true" class="fa fa-battery"></i>'],
        ['fa-battery-0', '<i aria-hidden="true" class="fa fa-battery-0"></i>'],
        ['fa-battery-1', '<i aria-hidden="true" class="fa fa-battery-1"></i>'],
        ['fa-battery-2', '<i aria-hidden="true" class="fa fa-battery-2"></i>'],
        ['fa-battery-3', '<i aria-hidden="true" class="fa fa-battery-3"></i>'],
        ['fa-battery-4', '<i aria-hidden="true" class="fa fa-battery-4"></i>'],
        ['fa-battery-empty', '<i aria-hidden="true" class="fa fa-battery-empty"></i>'],
        ['fa-battery-full', '<i aria-hidden="true" class="fa fa-battery-full"></i>'],
        ['fa-battery-half', '<i aria-hidden="true" class="fa fa-battery-half"></i>'],
        ['fa-battery-quarter', '<i aria-hidden="true" class="fa fa-battery-quarter"></i>'],
        ['fa-battery-three-quarters', '<i aria-hidden="true" class="fa fa-battery-three-quarters"></i>'],
        ['fa-bed', '<i aria-hidden="true" class="fa fa-bed"></i>'],
        ['fa-beer', '<i aria-hidden="true" class="fa fa-beer"></i>'],
        ['fa-bell', '<i aria-hidden="true" class="fa fa-bell"></i>'],
        ['fa-bell-o', '<i aria-hidden="true" class="fa fa-bell-o"></i>'],
        ['fa-bell-slash', '<i aria-hidden="true" class="fa fa-bell-slash"></i>'],
        ['fa-bell-slash-o', '<i aria-hidden="true" class="fa fa-bell-slash-o"></i>'],
        ['fa-bicycle', '<i aria-hidden="true" class="fa fa-bicycle"></i>'],
        ['fa-binoculars', '<i aria-hidden="true" class="fa fa-binoculars"></i>'],
        ['fa-birthday-cake', '<i aria-hidden="true" class="fa fa-birthday-cake"></i>'],
        ['fa-blind', '<i aria-hidden="true" class="fa fa-blind"></i>'],
        ['fa-bluetooth', '<i aria-hidden="true" class="fa fa-bluetooth"></i>'],
        ['fa-bluetooth-b', '<i aria-hidden="true" class="fa fa-bluetooth-b"></i>'],
        ['fa-bolt', '<i aria-hidden="true" class="fa fa-bolt"></i>'],
        ['fa-bomb', '<i aria-hidden="true" class="fa fa-bomb"></i>'],
        ['fa-book', '<i aria-hidden="true" class="fa fa-book"></i>'],
        ['fa-bookmark', '<i aria-hidden="true" class="fa fa-bookmark"></i>'],
        ['fa-bookmark-o', '<i aria-hidden="true" class="fa fa-bookmark-o"></i>'],
        ['fa-braille', '<i aria-hidden="true" class="fa fa-braille"></i>'],
        ['fa-briefcase', '<i aria-hidden="true" class="fa fa-briefcase"></i>'],
        ['fa-bug', '<i aria-hidden="true" class="fa fa-bug"></i>'],
        ['fa-building', '<i aria-hidden="true" class="fa fa-building"></i>'],
        ['fa-building-o', '<i aria-hidden="true" class="fa fa-building-o"></i>'],
        ['fa-bullhorn', '<i aria-hidden="true" class="fa fa-bullhorn"></i>'],
        ['fa-bullseye', '<i aria-hidden="true" class="fa fa-bullseye"></i>'],
        ['fa-bus', '<i aria-hidden="true" class="fa fa-bus"></i>'],
        ['fa-cab', '<i aria-hidden="true" class="fa fa-cab"></i>'],
        ['fa-calculator', '<i aria-hidden="true" class="fa fa-calculator"></i>'],
        ['fa-calendar', '<i aria-hidden="true" class="fa fa-calendar"></i>'],
        ['fa-calendar-check-o', '<i aria-hidden="true" class="fa fa-calendar-check-o"></i>'],
        ['fa-calendar-minus-o', '<i aria-hidden="true" class="fa fa-calendar-minus-o"></i>'],
        ['fa-calendar-o', '<i aria-hidden="true" class="fa fa-calendar-o"></i>'],
        ['fa-calendar-plus-o', '<i aria-hidden="true" class="fa fa-calendar-plus-o"></i>'],
        ['fa-calendar-times-o', '<i aria-hidden="true" class="fa fa-calendar-times-o"></i>'],
        ['fa-camera', '<i aria-hidden="true" class="fa fa-camera"></i>'],
        ['fa-camera-retro', '<i aria-hidden="true" class="fa fa-camera-retro"></i>'],
        ['fa-car', '<i aria-hidden="true" class="fa fa-car"></i>'],
        ['fa-caret-square-o-down', '<i aria-hidden="true" class="fa fa-caret-square-o-down"></i>'],
        ['fa-caret-square-o-left', '<i aria-hidden="true" class="fa fa-caret-square-o-left"></i>'],
        ['fa-caret-square-o-right', '<i aria-hidden="true" class="fa fa-caret-square-o-right"></i>'],
        ['fa-caret-square-o-up', '<i aria-hidden="true" class="fa fa-caret-square-o-up"></i>'],
        ['fa-cart-arrow-down', '<i aria-hidden="true" class="fa fa-cart-arrow-down"></i>'],
        ['fa-cart-plus', '<i aria-hidden="true" class="fa fa-cart-plus"></i>'],
        ['fa-cc', '<i aria-hidden="true" class="fa fa-cc"></i>'],
        ['fa-certificate', '<i aria-hidden="true" class="fa fa-certificate"></i>'],
        ['fa-check', '<i aria-hidden="true" class="fa fa-check"></i>'],
        ['fa-check-circle', '<i aria-hidden="true" class="fa fa-check-circle"></i>'],
        ['fa-check-circle-o', '<i aria-hidden="true" class="fa fa-check-circle-o"></i>'],
        ['fa-check-square', '<i aria-hidden="true" class="fa fa-check-square"></i>'],
        ['fa-check-square-o', '<i aria-hidden="true" class="fa fa-check-square-o"></i>'],
        ['fa-child', '<i aria-hidden="true" class="fa fa-child"></i>'],
        ['fa-circle', '<i aria-hidden="true" class="fa fa-circle"></i>'],
        ['fa-circle-o', '<i aria-hidden="true" class="fa fa-circle-o"></i>'],
        ['fa-circle-o-notch', '<i aria-hidden="true" class="fa fa-circle-o-notch"></i>'],
        ['fa-circle-thin', '<i aria-hidden="true" class="fa fa-circle-thin"></i>'],
        ['fa-clock-o', '<i aria-hidden="true" class="fa fa-clock-o"></i>'],
        ['fa-clone', '<i aria-hidden="true" class="fa fa-clone"></i>'],
        ['fa-close', '<i aria-hidden="true" class="fa fa-close"></i>'],
        ['fa-cloud', '<i aria-hidden="true" class="fa fa-cloud"></i>'],
        ['fa-cloud-download', '<i aria-hidden="true" class="fa fa-cloud-download"></i>'],
        ['fa-cloud-upload', '<i aria-hidden="true" class="fa fa-cloud-upload"></i>'],
        ['fa-code', '<i aria-hidden="true" class="fa fa-code"></i>'],
        ['fa-code-fork', '<i aria-hidden="true" class="fa fa-code-fork"></i>'],
        ['fa-coffee', '<i aria-hidden="true" class="fa fa-coffee"></i>'],
        ['fa-cog', '<i aria-hidden="true" class="fa fa-cog"></i>'],
        ['fa-cogs', '<i aria-hidden="true" class="fa fa-cogs"></i>'],
        ['fa-comment', '<i aria-hidden="true" class="fa fa-comment"></i>'],
        ['fa-comment-o', '<i aria-hidden="true" class="fa fa-comment-o"></i>'],
        ['fa-commenting', '<i aria-hidden="true" class="fa fa-commenting"></i>'],
        ['fa-commenting-o', '<i aria-hidden="true" class="fa fa-commenting-o"></i>'],
        ['fa-comments', '<i aria-hidden="true" class="fa fa-comments"></i>'],
        ['fa-comments-o', '<i aria-hidden="true" class="fa fa-comments-o"></i>'],
        ['fa-compass', '<i aria-hidden="true" class="fa fa-compass"></i>'],
        ['fa-copyright', '<i aria-hidden="true" class="fa fa-copyright"></i>'],
        ['fa-creative-commons', '<i aria-hidden="true" class="fa fa-creative-commons"></i>'],
        ['fa-credit-card', '<i aria-hidden="true" class="fa fa-credit-card"></i>'],
        ['fa-credit-card-alt', '<i aria-hidden="true" class="fa fa-credit-card-alt"></i>'],
        ['fa-crop', '<i aria-hidden="true" class="fa fa-crop"></i>'],
        ['fa-crosshairs', '<i aria-hidden="true" class="fa fa-crosshairs"></i>'],
        ['fa-cube', '<i aria-hidden="true" class="fa fa-cube"></i>'],
        ['fa-cubes', '<i aria-hidden="true" class="fa fa-cubes"></i>'],
        ['fa-cutlery', '<i aria-hidden="true" class="fa fa-cutlery"></i>'],
        ['fa-dashboard', '<i aria-hidden="true" class="fa fa-dashboard"></i>'],
        ['fa-database', '<i aria-hidden="true" class="fa fa-database"></i>'],
        ['fa-deaf', '<i aria-hidden="true" class="fa fa-deaf"></i>'],
        ['fa-deafness', '<i aria-hidden="true" class="fa fa-deafness"></i>'],
        ['fa-desktop', '<i aria-hidden="true" class="fa fa-desktop"></i>'],
        ['fa-diamond', '<i aria-hidden="true" class="fa fa-diamond"></i>'],
        ['fa-dot-circle-o', '<i aria-hidden="true" class="fa fa-dot-circle-o"></i>'],
        ['fa-download', '<i aria-hidden="true" class="fa fa-download"></i>'],
        ['fa-drivers-license', '<i aria-hidden="true" class="fa fa-drivers-license"></i>'],
        ['fa-drivers-license-o', '<i aria-hidden="true" class="fa fa-drivers-license-o"></i>'],
        ['fa-edit', '<i aria-hidden="true" class="fa fa-edit"></i>'],
        ['fa-ellipsis-h', '<i aria-hidden="true" class="fa fa-ellipsis-h"></i>'],
        ['fa-ellipsis-v', '<i aria-hidden="true" class="fa fa-ellipsis-v"></i>'],
        ['fa-envelope', '<i aria-hidden="true" class="fa fa-envelope"></i>'],
        ['fa-envelope-o', '<i aria-hidden="true" class="fa fa-envelope-o"></i>'],
        ['fa-envelope-open', '<i aria-hidden="true" class="fa fa-envelope-open"></i>'],
        ['fa-envelope-open-o', '<i aria-hidden="true" class="fa fa-envelope-open-o"></i>'],
        ['fa-envelope-square', '<i aria-hidden="true" class="fa fa-envelope-square"></i>'],
        ['fa-eraser', '<i aria-hidden="true" class="fa fa-eraser"></i>'],
        ['fa-exchange', '<i aria-hidden="true" class="fa fa-exchange"></i>'],
        ['fa-exclamation', '<i aria-hidden="true" class="fa fa-exclamation"></i>'],
        ['fa-exclamation-circle', '<i aria-hidden="true" class="fa fa-exclamation-circle"></i>'],
        ['fa-exclamation-triangle', '<i aria-hidden="true" class="fa fa-exclamation-triangle"></i>'],
        ['fa-external-link', '<i aria-hidden="true" class="fa fa-external-link"></i>'],
        ['fa-external-link-square', '<i aria-hidden="true" class="fa fa-external-link-square"></i>'],
        ['fa-eye', '<i aria-hidden="true" class="fa fa-eye"></i>'],
        ['fa-eye-slash', '<i aria-hidden="true" class="fa fa-eye-slash"></i>'],
        ['fa-eyedropper', '<i aria-hidden="true" class="fa fa-eyedropper"></i>'],
        ['fa-fax', '<i aria-hidden="true" class="fa fa-fax"></i>'],
        ['fa-feed', '<i aria-hidden="true" class="fa fa-feed"></i>'],
        ['fa-female', '<i aria-hidden="true" class="fa fa-female"></i>'],
        ['fa-fighter-jet', '<i aria-hidden="true" class="fa fa-fighter-jet"></i>'],
        ['fa-file-archive-o', '<i aria-hidden="true" class="fa fa-file-archive-o"></i>'],
        ['fa-file-audio-o', '<i aria-hidden="true" class="fa fa-file-audio-o"></i>'],
        ['fa-file-code-o', '<i aria-hidden="true" class="fa fa-file-code-o"></i>'],
        ['fa-file-excel-o', '<i aria-hidden="true" class="fa fa-file-excel-o"></i>'],
        ['fa-file-image-o', '<i aria-hidden="true" class="fa fa-file-image-o"></i>'],
        ['fa-file-movie-o', '<i aria-hidden="true" class="fa fa-file-movie-o"></i>'],
        ['fa-file-pdf-o', '<i aria-hidden="true" class="fa fa-file-pdf-o"></i>'],
        ['fa-file-photo-o', '<i aria-hidden="true" class="fa fa-file-photo-o"></i>'],
        ['fa-file-picture-o', '<i aria-hidden="true" class="fa fa-file-picture-o"></i>'],
        ['fa-file-powerpoint-o', '<i aria-hidden="true" class="fa fa-file-powerpoint-o"></i>'],
        ['fa-file-sound-o', '<i aria-hidden="true" class="fa fa-file-sound-o"></i>'],
        ['fa-file-video-o', '<i aria-hidden="true" class="fa fa-file-video-o"></i>'],
        ['fa-file-word-o', '<i aria-hidden="true" class="fa fa-file-word-o"></i>'],
        ['fa-file-zip-o', '<i aria-hidden="true" class="fa fa-file-zip-o"></i>'],
        ['fa-film', '<i aria-hidden="true" class="fa fa-film"></i>'],
        ['fa-filter', '<i aria-hidden="true" class="fa fa-filter"></i>'],
        ['fa-fire', '<i aria-hidden="true" class="fa fa-fire"></i>'],
        ['fa-fire-extinguisher', '<i aria-hidden="true" class="fa fa-fire-extinguisher"></i>'],
        ['fa-flag', '<i aria-hidden="true" class="fa fa-flag"></i>'],
        ['fa-flag-checkered', '<i aria-hidden="true" class="fa fa-flag-checkered"></i>'],
        ['fa-flag-o', '<i aria-hidden="true" class="fa fa-flag-o"></i>'],
        ['fa-flash', '<i aria-hidden="true" class="fa fa-flash"></i>'],
        ['fa-flask', '<i aria-hidden="true" class="fa fa-flask"></i>'],
        ['fa-folder', '<i aria-hidden="true" class="fa fa-folder"></i>'],
        ['fa-folder-o', '<i aria-hidden="true" class="fa fa-folder-o"></i>'],
        ['fa-folder-open', '<i aria-hidden="true" class="fa fa-folder-open"></i>'],
        ['fa-folder-open-o', '<i aria-hidden="true" class="fa fa-folder-open-o"></i>'],
        ['fa-frown-o', '<i aria-hidden="true" class="fa fa-frown-o"></i>'],
        ['fa-futbol-o', '<i aria-hidden="true" class="fa fa-futbol-o"></i>'],
        ['fa-gamepad', '<i aria-hidden="true" class="fa fa-gamepad"></i>'],
        ['fa-gavel', '<i aria-hidden="true" class="fa fa-gavel"></i>'],
        ['fa-gear', '<i aria-hidden="true" class="fa fa-gear"></i>'],
        ['fa-gears', '<i aria-hidden="true" class="fa fa-gears"></i>'],
        ['fa-gift', '<i aria-hidden="true" class="fa fa-gift"></i>'],
        ['fa-glass', '<i aria-hidden="true" class="fa fa-glass"></i>'],
        ['fa-globe', '<i aria-hidden="true" class="fa fa-globe"></i>'],
        ['fa-graduation-cap', '<i aria-hidden="true" class="fa fa-graduation-cap"></i>'],
        ['fa-group', '<i aria-hidden="true" class="fa fa-group"></i>'],
        ['fa-hand-grab-o', '<i aria-hidden="true" class="fa fa-hand-grab-o"></i>'],
        ['fa-hand-lizard-o', '<i aria-hidden="true" class="fa fa-hand-lizard-o"></i>'],
        ['fa-hand-paper-o', '<i aria-hidden="true" class="fa fa-hand-paper-o"></i>'],
        ['fa-hand-peace-o', '<i aria-hidden="true" class="fa fa-hand-peace-o"></i>'],
        ['fa-hand-pointer-o', '<i aria-hidden="true" class="fa fa-hand-pointer-o"></i>'],
        ['fa-hand-rock-o', '<i aria-hidden="true" class="fa fa-hand-rock-o"></i>'],
        ['fa-hand-scissors-o', '<i aria-hidden="true" class="fa fa-hand-scissors-o"></i>'],
        ['fa-hand-spock-o', '<i aria-hidden="true" class="fa fa-hand-spock-o"></i>'],
        ['fa-hand-stop-o', '<i aria-hidden="true" class="fa fa-hand-stop-o"></i>'],
        ['fa-handshake-o', '<i aria-hidden="true" class="fa fa-handshake-o"></i>'],
        ['fa-hard-of-hearing', '<i aria-hidden="true" class="fa fa-hard-of-hearing"></i>'],
        ['fa-hashtag', '<i aria-hidden="true" class="fa fa-hashtag"></i>'],
        ['fa-hdd-o', '<i aria-hidden="true" class="fa fa-hdd-o"></i>'],
        ['fa-headphones', '<i aria-hidden="true" class="fa fa-headphones"></i>'],
        ['fa-heart', '<i aria-hidden="true" class="fa fa-heart"></i>'],
        ['fa-heart-o', '<i aria-hidden="true" class="fa fa-heart-o"></i>'],
        ['fa-heartbeat', '<i aria-hidden="true" class="fa fa-heartbeat"></i>'],
        ['fa-history', '<i aria-hidden="true" class="fa fa-history"></i>'],
        ['fa-home', '<i aria-hidden="true" class="fa fa-home"></i>'],
        ['fa-hotel', '<i aria-hidden="true" class="fa fa-hotel"></i>'],
        ['fa-hourglass', '<i aria-hidden="true" class="fa fa-hourglass"></i>'],
        ['fa-hourglass-1', '<i aria-hidden="true" class="fa fa-hourglass-1"></i>'],
        ['fa-hourglass-2', '<i aria-hidden="true" class="fa fa-hourglass-2"></i>'],
        ['fa-hourglass-3', '<i aria-hidden="true" class="fa fa-hourglass-3"></i>'],
        ['fa-hourglass-end', '<i aria-hidden="true" class="fa fa-hourglass-end"></i>'],
        ['fa-hourglass-half', '<i aria-hidden="true" class="fa fa-hourglass-half"></i>'],
        ['fa-hourglass-o', '<i aria-hidden="true" class="fa fa-hourglass-o"></i>'],
        ['fa-hourglass-start', '<i aria-hidden="true" class="fa fa-hourglass-start"></i>'],
        ['fa-i-cursor', '<i aria-hidden="true" class="fa fa-i-cursor"></i>'],
        ['fa-id-badge', '<i aria-hidden="true" class="fa fa-id-badge"></i>'],
        ['fa-id-card', '<i aria-hidden="true" class="fa fa-id-card"></i>'],
        ['fa-id-card-o', '<i aria-hidden="true" class="fa fa-id-card-o"></i>'],
        ['fa-image', '<i aria-hidden="true" class="fa fa-image"></i>'],
        ['fa-inbox', '<i aria-hidden="true" class="fa fa-inbox"></i>'],
        ['fa-industry', '<i aria-hidden="true" class="fa fa-industry"></i>'],
        ['fa-info', '<i aria-hidden="true" class="fa fa-info"></i>'],
        ['fa-info-circle', '<i aria-hidden="true" class="fa fa-info-circle"></i>'],
        ['fa-institution', '<i aria-hidden="true" class="fa fa-institution"></i>'],
        ['fa-key', '<i aria-hidden="true" class="fa fa-key"></i>'],
        ['fa-keyboard-o', '<i aria-hidden="true" class="fa fa-keyboard-o"></i>'],
        ['fa-language', '<i aria-hidden="true" class="fa fa-language"></i>'],
        ['fa-laptop', '<i aria-hidden="true" class="fa fa-laptop"></i>'],
        ['fa-leaf', '<i aria-hidden="true" class="fa fa-leaf"></i>'],
        ['fa-legal', '<i aria-hidden="true" class="fa fa-legal"></i>'],
        ['fa-lemon-o', '<i aria-hidden="true" class="fa fa-lemon-o"></i>'],
        ['fa-level-down', '<i aria-hidden="true" class="fa fa-level-down"></i>'],
        ['fa-level-up', '<i aria-hidden="true" class="fa fa-level-up"></i>'],
        ['fa-life-bouy', '<i aria-hidden="true" class="fa fa-life-bouy"></i>'],
        ['fa-life-buoy', '<i aria-hidden="true" class="fa fa-life-buoy"></i>'],
        ['fa-life-ring', '<i aria-hidden="true" class="fa fa-life-ring"></i>'],
        ['fa-life-saver', '<i aria-hidden="true" class="fa fa-life-saver"></i>'],
        ['fa-lightbulb-o', '<i aria-hidden="true" class="fa fa-lightbulb-o"></i>'],
        ['fa-line-chart', '<i aria-hidden="true" class="fa fa-line-chart"></i>'],
        ['fa-location-arrow', '<i aria-hidden="true" class="fa fa-location-arrow"></i>'],
        ['fa-lock', '<i aria-hidden="true" class="fa fa-lock"></i>'],
        ['fa-low-vision', '<i aria-hidden="true" class="fa fa-low-vision"></i>'],
        ['fa-magic', '<i aria-hidden="true" class="fa fa-magic"></i>'],
        ['fa-magnet', '<i aria-hidden="true" class="fa fa-magnet"></i>'],
        ['fa-mail-forward', '<i aria-hidden="true" class="fa fa-mail-forward"></i>'],
        ['fa-mail-reply', '<i aria-hidden="true" class="fa fa-mail-reply"></i>'],
        ['fa-mail-reply-all', '<i aria-hidden="true" class="fa fa-mail-reply-all"></i>'],
        ['fa-male', '<i aria-hidden="true" class="fa fa-male"></i>'],
        ['fa-map', '<i aria-hidden="true" class="fa fa-map"></i>'],
        ['fa-map-marker', '<i aria-hidden="true" class="fa fa-map-marker"></i>'],
        ['fa-map-o', '<i aria-hidden="true" class="fa fa-map-o"></i>'],
        ['fa-map-pin', '<i aria-hidden="true" class="fa fa-map-pin"></i>'],
        ['fa-map-signs', '<i aria-hidden="true" class="fa fa-map-signs"></i>'],
        ['fa-meh-o', '<i aria-hidden="true" class="fa fa-meh-o"></i>'],
        ['fa-microchip', '<i aria-hidden="true" class="fa fa-microchip"></i>'],
        ['fa-microphone', '<i aria-hidden="true" class="fa fa-microphone"></i>'],
        ['fa-microphone-slash', '<i aria-hidden="true" class="fa fa-microphone-slash"></i>'],
        ['fa-minus', '<i aria-hidden="true" class="fa fa-minus"></i>'],
        ['fa-minus-circle', '<i aria-hidden="true" class="fa fa-minus-circle"></i>'],
        ['fa-minus-square', '<i aria-hidden="true" class="fa fa-minus-square"></i>'],
        ['fa-minus-square-o', '<i aria-hidden="true" class="fa fa-minus-square-o"></i>'],
        ['fa-mobile', '<i aria-hidden="true" class="fa fa-mobile"></i>'],
        ['fa-mobile-phone', '<i aria-hidden="true" class="fa fa-mobile-phone"></i>'],
        ['fa-money', '<i aria-hidden="true" class="fa fa-money"></i>'],
        ['fa-moon-o', '<i aria-hidden="true" class="fa fa-moon-o"></i>'],
        ['fa-mortar-board', '<i aria-hidden="true" class="fa fa-mortar-board"></i>'],
        ['fa-motorcycle', '<i aria-hidden="true" class="fa fa-motorcycle"></i>'],
        ['fa-mouse-pointer', '<i aria-hidden="true" class="fa fa-mouse-pointer"></i>'],
        ['fa-music', '<i aria-hidden="true" class="fa fa-music"></i>'],
        ['fa-navicon', '<i aria-hidden="true" class="fa fa-navicon"></i>'],
        ['fa-newspaper-o', '<i aria-hidden="true" class="fa fa-newspaper-o"></i>'],
        ['fa-object-group', '<i aria-hidden="true" class="fa fa-object-group"></i>'],
        ['fa-object-ungroup', '<i aria-hidden="true" class="fa fa-object-ungroup"></i>'],
        ['fa-paint-brush', '<i aria-hidden="true" class="fa fa-paint-brush"></i>'],
        ['fa-paper-plane', '<i aria-hidden="true" class="fa fa-paper-plane"></i>'],
        ['fa-paper-plane-o', '<i aria-hidden="true" class="fa fa-paper-plane-o"></i>'],
        ['fa-paw', '<i aria-hidden="true" class="fa fa-paw"></i>'],
        ['fa-pencil', '<i aria-hidden="true" class="fa fa-pencil"></i>'],
        ['fa-pencil-square', '<i aria-hidden="true" class="fa fa-pencil-square"></i>'],
        ['fa-pencil-square-o', '<i aria-hidden="true" class="fa fa-pencil-square-o"></i>'],
        ['fa-percent', '<i aria-hidden="true" class="fa fa-percent"></i>'],
        ['fa-phone', '<i aria-hidden="true" class="fa fa-phone"></i>'],
        ['fa-phone-square', '<i aria-hidden="true" class="fa fa-phone-square"></i>'],
        ['fa-photo', '<i aria-hidden="true" class="fa fa-photo"></i>'],
        ['fa-picture-o', '<i aria-hidden="true" class="fa fa-picture-o"></i>'],
        ['fa-pie-chart', '<i aria-hidden="true" class="fa fa-pie-chart"></i>'],
        ['fa-plane', '<i aria-hidden="true" class="fa fa-plane"></i>'],
        ['fa-plug', '<i aria-hidden="true" class="fa fa-plug"></i>'],
        ['fa-plus', '<i aria-hidden="true" class="fa fa-plus"></i>'],
        ['fa-plus-circle', '<i aria-hidden="true" class="fa fa-plus-circle"></i>'],
        ['fa-plus-square', '<i aria-hidden="true" class="fa fa-plus-square"></i>'],
        ['fa-plus-square-o', '<i aria-hidden="true" class="fa fa-plus-square-o"></i>'],
        ['fa-podcast', '<i aria-hidden="true" class="fa fa-podcast"></i>'],
        ['fa-power-off', '<i aria-hidden="true" class="fa fa-power-off"></i>'],
        ['fa-print', '<i aria-hidden="true" class="fa fa-print"></i>'],
        ['fa-puzzle-piece', '<i aria-hidden="true" class="fa fa-puzzle-piece"></i>'],
        ['fa-qrcode', '<i aria-hidden="true" class="fa fa-qrcode"></i>'],
        ['fa-question', '<i aria-hidden="true" class="fa fa-question"></i>'],
        ['fa-question-circle', '<i aria-hidden="true" class="fa fa-question-circle"></i>'],
        ['fa-question-circle-o', '<i aria-hidden="true" class="fa fa-question-circle-o"></i>'],
        ['fa-quote-left', '<i aria-hidden="true" class="fa fa-quote-left"></i>'],
        ['fa-quote-right', '<i aria-hidden="true" class="fa fa-quote-right"></i>'],
        ['fa-random', '<i aria-hidden="true" class="fa fa-random"></i>'],
        ['fa-recycle', '<i aria-hidden="true" class="fa fa-recycle"></i>'],
        ['fa-refresh', '<i aria-hidden="true" class="fa fa-refresh"></i>'],
        ['fa-registered', '<i aria-hidden="true" class="fa fa-registered"></i>'],
        ['fa-remove', '<i aria-hidden="true" class="fa fa-remove"></i>'],
        ['fa-reorder', '<i aria-hidden="true" class="fa fa-reorder"></i>'],
        ['fa-reply', '<i aria-hidden="true" class="fa fa-reply"></i>'],
        ['fa-reply-all', '<i aria-hidden="true" class="fa fa-reply-all"></i>'],
        ['fa-retweet', '<i aria-hidden="true" class="fa fa-retweet"></i>'],
        ['fa-road', '<i aria-hidden="true" class="fa fa-road"></i>'],
        ['fa-rocket', '<i aria-hidden="true" class="fa fa-rocket"></i>'],
        ['fa-rss', '<i aria-hidden="true" class="fa fa-rss"></i>'],
        ['fa-rss-square', '<i aria-hidden="true" class="fa fa-rss-square"></i>'],
        ['fa-s15', '<i aria-hidden="true" class="fa fa-s15"></i>'],
        ['fa-search', '<i aria-hidden="true" class="fa fa-search"></i>'],
        ['fa-search-minus', '<i aria-hidden="true" class="fa fa-search-minus"></i>'],
        ['fa-search-plus', '<i aria-hidden="true" class="fa fa-search-plus"></i>'],
        ['fa-send', '<i aria-hidden="true" class="fa fa-send"></i>'],
        ['fa-send-o', '<i aria-hidden="true" class="fa fa-send-o"></i>'],
        ['fa-server', '<i aria-hidden="true" class="fa fa-server"></i>'],
        ['fa-share', '<i aria-hidden="true" class="fa fa-share"></i>'],
        ['fa-share-alt', '<i aria-hidden="true" class="fa fa-share-alt"></i>'],
        ['fa-share-alt-square', '<i aria-hidden="true" class="fa fa-share-alt-square"></i>'],
        ['fa-share-square', '<i aria-hidden="true" class="fa fa-share-square"></i>'],
        ['fa-share-square-o', '<i aria-hidden="true" class="fa fa-share-square-o"></i>'],
        ['fa-shield', '<i aria-hidden="true" class="fa fa-shield"></i>'],
        ['fa-ship', '<i aria-hidden="true" class="fa fa-ship"></i>'],
        ['fa-shopping-bag', '<i aria-hidden="true" class="fa fa-shopping-bag"></i>'],
        ['fa-shopping-basket', '<i aria-hidden="true" class="fa fa-shopping-basket"></i>'],
        ['fa-shopping-cart', '<i aria-hidden="true" class="fa fa-shopping-cart"></i>'],
        ['fa-shower', '<i aria-hidden="true" class="fa fa-shower"></i>'],
        ['fa-sign-in', '<i aria-hidden="true" class="fa fa-sign-in"></i>'],
        ['fa-sign-language', '<i aria-hidden="true" class="fa fa-sign-language"></i>'],
        ['fa-sign-out', '<i aria-hidden="true" class="fa fa-sign-out"></i>'],
        ['fa-signal', '<i aria-hidden="true" class="fa fa-signal"></i>'],
        ['fa-signing', '<i aria-hidden="true" class="fa fa-signing"></i>'],
        ['fa-sitemap', '<i aria-hidden="true" class="fa fa-sitemap"></i>'],
        ['fa-sliders', '<i aria-hidden="true" class="fa fa-sliders"></i>'],
        ['fa-smile-o', '<i aria-hidden="true" class="fa fa-smile-o"></i>'],
        ['fa-snowflake-o', '<i aria-hidden="true" class="fa fa-snowflake-o"></i>'],
        ['fa-soccer-ball-o', '<i aria-hidden="true" class="fa fa-soccer-ball-o"></i>'],
        ['fa-sort', '<i aria-hidden="true" class="fa fa-sort"></i>'],
        ['fa-sort-alpha-asc', '<i aria-hidden="true" class="fa fa-sort-alpha-asc"></i>'],
        ['fa-sort-alpha-desc', '<i aria-hidden="true" class="fa fa-sort-alpha-desc"></i>'],
        ['fa-sort-amount-asc', '<i aria-hidden="true" class="fa fa-sort-amount-asc"></i>'],
        ['fa-sort-amount-desc', '<i aria-hidden="true" class="fa fa-sort-amount-desc"></i>'],
        ['fa-sort-asc', '<i aria-hidden="true" class="fa fa-sort-asc"></i>'],
        ['fa-sort-desc', '<i aria-hidden="true" class="fa fa-sort-desc"></i>'],
        ['fa-sort-down', '<i aria-hidden="true" class="fa fa-sort-down"></i>'],
        ['fa-sort-numeric-asc', '<i aria-hidden="true" class="fa fa-sort-numeric-asc"></i>'],
        ['fa-sort-numeric-desc', '<i aria-hidden="true" class="fa fa-sort-numeric-desc"></i>'],
        ['fa-sort-up', '<i aria-hidden="true" class="fa fa-sort-up"></i>'],
        ['fa-space-shuttle', '<i aria-hidden="true" class="fa fa-space-shuttle"></i>'],
        ['fa-spinner', '<i aria-hidden="true" class="fa fa-spinner"></i>'],
        ['fa-spoon', '<i aria-hidden="true" class="fa fa-spoon"></i>'],
        ['fa-square', '<i aria-hidden="true" class="fa fa-square"></i>'],
        ['fa-square-o', '<i aria-hidden="true" class="fa fa-square-o"></i>'],
        ['fa-star', '<i aria-hidden="true" class="fa fa-star"></i>'],
        ['fa-star-half', '<i aria-hidden="true" class="fa fa-star-half"></i>'],
        ['fa-star-half-empty', '<i aria-hidden="true" class="fa fa-star-half-empty"></i>'],
        ['fa-star-half-full', '<i aria-hidden="true" class="fa fa-star-half-full"></i>'],
        ['fa-star-half-o', '<i aria-hidden="true" class="fa fa-star-half-o"></i>'],
        ['fa-star-o', '<i aria-hidden="true" class="fa fa-star-o"></i>'],
        ['fa-sticky-note', '<i aria-hidden="true" class="fa fa-sticky-note"></i>'],
        ['fa-sticky-note-o', '<i aria-hidden="true" class="fa fa-sticky-note-o"></i>'],
        ['fa-street-view', '<i aria-hidden="true" class="fa fa-street-view"></i>'],
        ['fa-suitcase', '<i aria-hidden="true" class="fa fa-suitcase"></i>'],
        ['fa-sun-o', '<i aria-hidden="true" class="fa fa-sun-o"></i>'],
        ['fa-support', '<i aria-hidden="true" class="fa fa-support"></i>'],
        ['fa-tablet', '<i aria-hidden="true" class="fa fa-tablet"></i>'],
        ['fa-tachometer', '<i aria-hidden="true" class="fa fa-tachometer"></i>'],
        ['fa-tag', '<i aria-hidden="true" class="fa fa-tag"></i>'],
        ['fa-tags', '<i aria-hidden="true" class="fa fa-tags"></i>'],
        ['fa-tasks', '<i aria-hidden="true" class="fa fa-tasks"></i>'],
        ['fa-taxi', '<i aria-hidden="true" class="fa fa-taxi"></i>'],
        ['fa-television', '<i aria-hidden="true" class="fa fa-television"></i>'],
        ['fa-terminal', '<i aria-hidden="true" class="fa fa-terminal"></i>'],
        ['fa-thermometer', '<i aria-hidden="true" class="fa fa-thermometer"></i>'],
        ['fa-thermometer-0', '<i aria-hidden="true" class="fa fa-thermometer-0"></i>'],
        ['fa-thermometer-1', '<i aria-hidden="true" class="fa fa-thermometer-1"></i>'],
        ['fa-thermometer-2', '<i aria-hidden="true" class="fa fa-thermometer-2"></i>'],
        ['fa-thermometer-3', '<i aria-hidden="true" class="fa fa-thermometer-3"></i>'],
        ['fa-thermometer-4', '<i aria-hidden="true" class="fa fa-thermometer-4"></i>'],
        ['fa-thermometer-empty', '<i aria-hidden="true" class="fa fa-thermometer-empty"></i>'],
        ['fa-thermometer-full', '<i aria-hidden="true" class="fa fa-thermometer-full"></i>'],
        ['fa-thermometer-half', '<i aria-hidden="true" class="fa fa-thermometer-half"></i>'],
        ['fa-thermometer-quarter', '<i aria-hidden="true" class="fa fa-thermometer-quarter"></i>'],
        ['fa-thermometer-three-quarters',
         '<i aria-hidden="true" class="fa fa-thermometer-three-quarters"></i>'],
        ['fa-thumb-tack', '<i aria-hidden="true" class="fa fa-thumb-tack"></i>'],
        ['fa-thumbs-down', '<i aria-hidden="true" class="fa fa-thumbs-down"></i>'],
        ['fa-thumbs-o-down', '<i aria-hidden="true" class="fa fa-thumbs-o-down"></i>'],
        ['fa-thumbs-o-up', '<i aria-hidden="true" class="fa fa-thumbs-o-up"></i>'],
        ['fa-thumbs-up', '<i aria-hidden="true" class="fa fa-thumbs-up"></i>'],
        ['fa-ticket', '<i aria-hidden="true" class="fa fa-ticket"></i>'],
        ['fa-times', '<i aria-hidden="true" class="fa fa-times"></i>'],
        ['fa-times-circle', '<i aria-hidden="true" class="fa fa-times-circle"></i>'],
        ['fa-times-circle-o', '<i aria-hidden="true" class="fa fa-times-circle-o"></i>'],
        ['fa-times-rectangle', '<i aria-hidden="true" class="fa fa-times-rectangle"></i>'],
        ['fa-times-rectangle-o', '<i aria-hidden="true" class="fa fa-times-rectangle-o"></i>'],
        ['fa-tint', '<i aria-hidden="true" class="fa fa-tint"></i>'],
        ['fa-toggle-down', '<i aria-hidden="true" class="fa fa-toggle-down"></i>'],
        ['fa-toggle-left', '<i aria-hidden="true" class="fa fa-toggle-left"></i>'],
        ['fa-toggle-off', '<i aria-hidden="true" class="fa fa-toggle-off"></i>'],
        ['fa-toggle-on', '<i aria-hidden="true" class="fa fa-toggle-on"></i>'],
        ['fa-toggle-right', '<i aria-hidden="true" class="fa fa-toggle-right"></i>'],
        ['fa-toggle-up', '<i aria-hidden="true" class="fa fa-toggle-up"></i>'],
        ['fa-trademark', '<i aria-hidden="true" class="fa fa-trademark"></i>'],
        ['fa-trash', '<i aria-hidden="true" class="fa fa-trash"></i>'],
        ['fa-trash-o', '<i aria-hidden="true" class="fa fa-trash-o"></i>'],
        ['fa-tree', '<i aria-hidden="true" class="fa fa-tree"></i>'],
        ['fa-trophy', '<i aria-hidden="true" class="fa fa-trophy"></i>'],
        ['fa-truck', '<i aria-hidden="true" class="fa fa-truck"></i>'],
        ['fa-tty', '<i aria-hidden="true" class="fa fa-tty"></i>'],
        ['fa-tv', '<i aria-hidden="true" class="fa fa-tv"></i>'],
        ['fa-umbrella', '<i aria-hidden="true" class="fa fa-umbrella"></i>'],
        ['fa-universal-access', '<i aria-hidden="true" class="fa fa-universal-access"></i>'],
        ['fa-university', '<i aria-hidden="true" class="fa fa-university"></i>'],
        ['fa-unlock', '<i aria-hidden="true" class="fa fa-unlock"></i>'],
        ['fa-unlock-alt', '<i aria-hidden="true" class="fa fa-unlock-alt"></i>'],
        ['fa-unsorted', '<i aria-hidden="true" class="fa fa-unsorted"></i>'],
        ['fa-upload', '<i aria-hidden="true" class="fa fa-upload"></i>'],
        ['fa-user', '<i aria-hidden="true" class="fa fa-user"></i>'],
        ['fa-user-circle', '<i aria-hidden="true" class="fa fa-user-circle"></i>'],
        ['fa-user-circle-o', '<i aria-hidden="true" class="fa fa-user-circle-o"></i>'],
        ['fa-user-o', '<i aria-hidden="true" class="fa fa-user-o"></i>'],
        ['fa-user-plus', '<i aria-hidden="true" class="fa fa-user-plus"></i>'],
        ['fa-user-secret', '<i aria-hidden="true" class="fa fa-user-secret"></i>'],
        ['fa-user-times', '<i aria-hidden="true" class="fa fa-user-times"></i>'],
        ['fa-users', '<i aria-hidden="true" class="fa fa-users"></i>'],
        ['fa-vcard', '<i aria-hidden="true" class="fa fa-vcard"></i>'],
        ['fa-vcard-o', '<i aria-hidden="true" class="fa fa-vcard-o"></i>'],
        ['fa-video-camera', '<i aria-hidden="true" class="fa fa-video-camera"></i>'],
        ['fa-volume-control-phone', '<i aria-hidden="true" class="fa fa-volume-control-phone"></i>'],
        ['fa-volume-down', '<i aria-hidden="true" class="fa fa-volume-down"></i>'],
        ['fa-volume-off', '<i aria-hidden="true" class="fa fa-volume-off"></i>'],
        ['fa-volume-up', '<i aria-hidden="true" class="fa fa-volume-up"></i>'],
        ['fa-warning', '<i aria-hidden="true" class="fa fa-warning"></i>'],
        ['fa-wheelchair', '<i aria-hidden="true" class="fa fa-wheelchair"></i>'],
        ['fa-wheelchair-alt', '<i aria-hidden="true" class="fa fa-wheelchair-alt"></i>'],
        ['fa-wifi', '<i aria-hidden="true" class="fa fa-wifi"></i>'],
        ['fa-window-close', '<i aria-hidden="true" class="fa fa-window-close"></i>'],
        ['fa-window-close-o', '<i aria-hidden="true" class="fa fa-window-close-o"></i>'],
        ['fa-window-maximize', '<i aria-hidden="true" class="fa fa-window-maximize"></i>'],
        ['fa-window-minimize', '<i aria-hidden="true" class="fa fa-window-minimize"></i>'],
        ['fa-window-restore', '<i aria-hidden="true" class="fa fa-window-restore"></i>'],
        ['fa-wrench', '<i aria-hidden="true" class="fa fa-wrench"></i>']]

ICON_CHOICES = [[i[0], mark_safe(i[1])] for i in data]


class MenuForm(BsModelForm):
    class Meta:
        model = models.Menu
        fields = ['title', 'weight', 'icon']
        widgets = {
            'icon': forms.RadioSelect(choices=ICON_CHOICES)
        }


class PermissionForm(BsModelForm):
    class Meta:
        model = models.Permission
        fields = '__all__'
        labels = {
            'menu': '所属菜单',
            'parent': '父权限', }

    def __init__(self, *args, **kwargs):
        super(PermissionForm, self).__init__(*args, **kwargs)
        objs = models.Permission.objects.filter(menu_id__isnull=False)
        self.fields['parent'].choices = [('', '---------')] + [(i.pk, i) for i in objs]
