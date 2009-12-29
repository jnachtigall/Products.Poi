# Permissions used by Poi

from Products.CMFCore import permissions as CMFCorePermissions

View                      = CMFCorePermissions.View
ModifyPortalContent       = CMFCorePermissions.ModifyPortalContent
AccessContentsInformation = CMFCorePermissions.AccessContentsInformation

ManageTracker             = "Poi: Manage tracker"
EditResponse              = "Poi: Edit response"
ModifyIssueSeverity       = "Poi: Modify issue severity"
ModifyIssueAssignment     = "Poi: Modify issue assignment"
ModifyIssueState          = "Poi: Modify issue state"
ModifyIssueTags           = "Poi: Modify issue tags"
ModifyIssueWatchers       = "Poi: Modify issue watchers"
ModifyIssueTargetRelease  = "Poi: Modify issue target release"
UploadAttachment          = "Poi: Upload attachment"
