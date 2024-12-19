# ---+ Extensions
# ---++ AutoRedirectPlugin
# This is the configuration used by the <b>AutoRedirectPlugin</b>.

# **PERL CHECK="undefok emptyok"**
# Rules to trigger a redirect.
$Foswiki::cfg{Plugins}{AutoRedirectPlugin}{Rules} = [
  {
    'context' => 'register',
    'target' => 'none',
  },
  { 
    'context' => 'isadmin',
    'target' => 'none'
  },
  {
    'web' => '_.*',
    'target' => 'Main.WebHome',
  },
  {
    'wikiName' => 'WikiGuest',
    'web' => 'Applications.*',
    'target' => 'Main.WebHome',
  },
  {
    'wikiName' => 'WikiGuest',
    'topic' => 'SitePreferences|WebPreferences|WebStatistics|WebTopicList|WebIndex|WebNotify|WebStatistics|WebTopicEditTemplate|WebChanges|SiteChanges|SeoTopic|ClassifiedTopic|WikiTopic|Category',
    'target' => 'WebHome',
  },
  {
    'web' => 'System',
    'topic' => 'InstalledPlugins|LicensePlugin|PerlDependencyReport|Contribs|FoswikiServerInformation|PerlDoc',
    'target' => 'Main.WebHome',
  },
  {
    'web' => 'System',
    'topic' => 'UserRegistration|ResetPassword|ChangeEmailAddress|ChangePassword',
    'target' => 'none',
  },
  {
    'wikiName' => 'WikiGuest',
    'web' => 'System',
    'target' => 'Main.WebHome',
  },
];

1;
