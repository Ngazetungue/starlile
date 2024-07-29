from django.contrib import admin
from .models import Team, Fixture, Result, Player, Story, News, Tv, CAF, Premiership, NFACup

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo')
    search_fields = ('name',)

class FixtureAdmin(admin.ModelAdmin):
    list_display = ('home', 'away', 'date', 'time', 'stadium', 'town')
    list_filter = ('date', 'stadium', 'town')
    search_fields = ('home__name', 'away__name', 'stadium', 'town')

class ResultAdmin(admin.ModelAdmin):
    list_display = ('fixture', 'home_score', 'away_score', 'home_team', 'away_team')
    search_fields = ('fixture__home__name', 'fixture__away__name')
    
    def home_team(self, obj):
        return obj.home_team
    
    def away_team(self, obj):
        return obj.away_team

    home_team.short_description = 'Home Team'
    away_team.short_description = 'Away Team'
    
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'age', 'country', 'position', 'shirt_number', 'joined', 'debut', 'appearances', 'goals')
    search_fields = ('first_name', 'last_name', 'country', 'position')
    list_filter = ('position', 'country')
    ordering = ('last_name', 'first_name')
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'photo', 'date_of_birth', 'country', 'position', 'bio', 'shirt_number', 'joined', 'debut')
        }),
        ('Statistics', {
            'fields': ('appearances', 'goals')
        }),
    )

class StoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title',)
    list_filter = ('date',)

class TvAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title',)
    list_filter = ('date',)

class CAFAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title',)
    list_filter = ('date',)

class PremiershipAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title',)
    list_filter = ('date',)

class NFACupAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title',)
    list_filter = ('date',)


admin.site.register(Team, TeamAdmin)
admin.site.register(Fixture, FixtureAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Story, StoryAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Tv, TvAdmin)
admin.site.register(CAF, CAFAdmin)
admin.site.register(Premiership, PremiershipAdmin)
admin.site.register(NFACup, NFACupAdmin)
