# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T09:48:55+00:00



import argparse
import json
import os
from typing import *

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import APIKeyHeader, APIKeyQuery, BaseSecurity
from fastapi import Path

from models import (
    BoxScore,
    CompetitionDetail,
    FieldFormatActiveMembershipsGetResponse,
    FieldFormatAreasGetResponse,
    FieldFormatBoxScoresByCompetitionCompetitionDateGetResponse,
    FieldFormatBoxScoresDateGetResponse,
    FieldFormatBoxScoresDeltaByCompetitionCompetitionDateMinutesGetResponse,
    FieldFormatBoxScoresDeltaDateMinutesGetResponse,
    FieldFormatCompetitionHierarchyGetResponse,
    FieldFormatCompetitionsGetResponse,
    FieldFormatDfsSlatesByDateDateGetResponse,
    FieldFormatGamesByDateDateGetResponse,
    FieldFormatHistoricalMembershipsByCompetitionCompetitionGetResponse,
    FieldFormatHistoricalMembershipsByTeamTeamidGetResponse,
    FieldFormatHistoricalMembershipsGetResponse,
    FieldFormatMembershipsByCompetitionCompetitionGetResponse,
    FieldFormatMembershipsByTeamTeamidGetResponse,
    FieldFormatPlayerGameStatsByDateDateGetResponse,
    FieldFormatPlayerGameStatsByPlayerDatePlayeridGetResponse,
    FieldFormatPlayersByTeamTeamidGetResponse,
    FieldFormatPlayerSeasonStatsByPlayerRoundidPlayeridGetResponse,
    FieldFormatPlayerSeasonStatsByTeamRoundidTeamGetResponse,
    FieldFormatPlayerSeasonStatsRoundidGetResponse,
    FieldFormatPlayersGetResponse,
    FieldFormatRecentlyChangedMembershipsDaysGetResponse,
    FieldFormatScheduleRoundidGetResponse,
    FieldFormatSeasonTeamsSeasonidGetResponse,
    FieldFormatStandingsRoundidGetResponse,
    FieldFormatTeamGameStatsByDateDateGetResponse,
    FieldFormatTeamSeasonStatsRoundidGetResponse,
    FieldFormatTeamsGetResponse,
    FieldFormatUpcomingDfsSlatesByCompetitionCompetitionIdGetResponse,
    FieldFormatUpcomingScheduleByPlayerPlayeridGetResponse,
    FieldFormatVenuesGetResponse,
    Format,
    Format10,
    Format11,
    Format32,
    Format33,
    Player,
)

app = MCPProxy(
    contact={'x-twitter': 'nfldata'},
    title='Soccer v3 Stats',
    version='1.0',
    servers=[
        {'url': 'http://azure-api.sportsdata.io/v3/soccer/stats'},
        {'url': 'https://azure-api.sportsdata.io/v3/soccer/stats'},
    ],
)


@app.get(
    '/{format}/ActiveMemberships',
    tags=['membership_management'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def memberships_active(format: Format = 'xml'):
    """
    Memberships (Active)
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/Areas',
    tags=[
        'membership_management',
        'competition_statistics',
        'game_statistics',
        'player_management',
        'team_statistics',
        'team_management',
        'fantasy_sports_schedule',
        'player_timeline_schedule',
        'venue_data',
    ],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def areas_countries(format: Format = 'xml'):
    """
    Areas (Countries)
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/BoxScore/{gameid}',
    tags=['game_statistics', 'competition_statistics'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def box_score(format: Format = 'xml', gameid: str = ...):
    """
    Box Score
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/BoxScores/{date}',
    tags=['game_statistics', 'competition_statistics'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def box_scores_by_date(format: Format = 'xml', date: str = ...):
    """
    Box Scores by Date
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/BoxScoresByCompetition/{competition}/{date}',
    tags=['competition_statistics', 'game_statistics'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def box_scores_by_date_by_competition(
    format: Format = 'xml', competition: str = ..., date: str = ...
):
    """
    Box Scores by Date by Competition
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/BoxScoresDelta/{date}/{minutes}',
    tags=['game_statistics', 'competition_statistics'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def box_scores_by_date_delta(
    format: Format = 'xml', date: str = ..., minutes: str = ...
):
    """
    Box Scores by Date Delta
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/BoxScoresDeltaByCompetition/{competition}/{date}/{minutes}',
    tags=['competition_statistics', 'game_statistics'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def box_scores_delta_by_date_by_competition(
    format: Format = 'xml', competition: str = ..., date: str = ..., minutes: str = ...
):
    """
    Box Scores Delta by Date by Competition
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/CompetitionDetails/{competition}',
    tags=['competition_statistics'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def competition_fixtures_league_details(format: Format = 'xml', competition: str = ...):
    """
    Competition Fixtures (League Details)
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/CompetitionHierarchy',
    tags=['competition_statistics'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def competition_hierarchy_league_hierarchy(format: Format = 'xml'):
    """
    Competition Hierarchy (League Hierarchy)
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/Competitions',
    tags=['competition_statistics', 'membership_management'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def competitions_leagues(format: Format = 'xml'):
    """
    Competitions (Leagues)
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/DfsSlatesByDate/{date}',
    tags=['fantasy_sports_schedule'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def dfs_slates_by_date(format: Format10, date: str = ...):
    """
    Dfs Slates By Date
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/GamesByDate/{date}',
    tags=['game_statistics', 'competition_statistics'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def games_by_date(format: Format11 = 'xml', date: str = ...):
    """
    Games by Date
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/HistoricalMemberships',
    tags=['membership_management'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def memberships_historical(format: Format11 = 'xml'):
    """
    Memberships (Historical)
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/HistoricalMembershipsByCompetition/{competition}',
    tags=['membership_management', 'competition_statistics'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def memberships_by_competition_historical(
    format: Format11 = 'xml', competition: str = ...
):
    """
    Memberships by Competition (Historical)
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/HistoricalMembershipsByTeam/{teamid}',
    tags=['membership_management'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def memberships_by_team_historical(format: Format11 = 'xml', teamid: str = ...):
    """
    Memberships by Team (Historical)
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/MembershipsByCompetition/{competition}',
    tags=['membership_management', 'competition_statistics'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def memberships_by_competition_active(format: Format11 = 'xml', competition: str = ...):
    """
    Memberships by Competition (Active)
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/MembershipsByTeam/{teamid}',
    tags=['membership_management', 'team_management'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def memberships_by_team_active(format: Format11 = 'xml', teamid: str = ...):
    """
    Memberships by Team (Active)
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/Player/{playerid}',
    tags=['player_management', 'game_statistics'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def player(format: Format11 = 'xml', playerid: str = ...):
    """
    Player
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/PlayerGameStatsByDate/{date}',
    tags=['game_statistics', 'player_management'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def player_game_stats_by_date(format: Format11 = 'xml', date: str = ...):
    """
    Player Game Stats by Date
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/PlayerGameStatsByPlayer/{date}/{playerid}',
    tags=['game_statistics', 'player_management'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def player_game_stats_by_player(
    format: Format11 = 'xml', date: str = ..., playerid: str = ...
):
    """
    Player Game Stats by Player
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/PlayerSeasonStats/{roundid}',
    tags=['competition_statistics', 'game_statistics', 'player_management'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def player_season_stats(format: Format11 = 'xml', roundid: str = ...):
    """
    Player Season Stats
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/PlayerSeasonStatsByPlayer/{roundid}/{playerid}',
    tags=['game_statistics', 'player_management'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def player_season_stats_by_player(
    format: Format11 = 'xml', roundid: str = ..., playerid: str = ...
):
    """
    Player Season Stats by Player
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/PlayerSeasonStatsByTeam/{roundid}/{team}',
    tags=[
        'competition_statistics',
        'game_statistics',
        'player_management',
        'team_statistics',
    ],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def player_season_stats_by_team(
    format: Format11 = 'xml', roundid: str = ..., team: str = ...
):
    """
    Player Season Stats by Team
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/Players',
    tags=['player_management'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def players(format: Format11 = 'xml'):
    """
    Players
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/PlayersByTeam/{teamid}',
    tags=['player_management', 'team_statistics'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def players_by_team(format: Format11 = 'xml', teamid: str = ...):
    """
    Players by Team
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/RecentlyChangedMemberships/{days}',
    tags=['membership_management'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def memberships_recently_changed(format: Format11 = 'xml', days: str = ...):
    """
    Memberships (Recently Changed)
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/Schedule/{roundid}',
    tags=['fantasy_sports_schedule', 'competition_statistics'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def schedule(format: Format11 = 'xml', roundid: str = ...):
    """
    Schedule
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/SeasonTeams/{seasonid}',
    tags=['competition_statistics', 'team_statistics', 'team_management'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def season_teams(format: Format11 = 'xml', seasonid: str = ...):
    """
    Season Teams
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/Standings/{roundid}',
    tags=['competition_statistics'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def standings(format: Format11 = 'xml', roundid: str = ...):
    """
    Standings
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/TeamGameStatsByDate/{date}',
    tags=['game_statistics', 'team_statistics'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def team_game_stats_by_date(format: Format11 = 'xml', date: str = ...):
    """
    Team Game Stats by Date
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/TeamSeasonStats/{roundid}',
    tags=['team_statistics', 'competition_statistics'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def team_season_stats(format: Format11 = 'xml', roundid: str = ...):
    """
    Team Season Stats
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/Teams',
    tags=['team_management', 'team_statistics'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def teams(format: Format11 = 'xml'):
    """
    Teams
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/UpcomingDfsSlatesByCompetition/{competitionId}',
    tags=['fantasy_sports_schedule', 'competition_statistics'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def upcoming_dfs_slates_by_competition(
    format: Format32, competition_id: str = Path(..., alias='competitionId')
):
    """
    Upcoming Dfs Slates By Competition
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/UpcomingScheduleByPlayer/{playerid}',
    tags=['player_management', 'player_timeline_schedule'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def upcoming_schedule_by_player(format: Format33 = 'xml', playerid: str = ...):
    """
    Upcoming Schedule By Player
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{format}/Venues',
    tags=['venue_data', 'team_management'],
    security=[
        APIKeyHeader(name="Ocp-Apim-Subscription-Key"),
        APIKeyQuery(name="key"),
    ],
)
def venues(format: Format33 = 'xml'):
    """
    Venues
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
