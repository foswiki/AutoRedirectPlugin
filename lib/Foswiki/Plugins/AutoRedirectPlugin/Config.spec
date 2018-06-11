# ---+ Extensions
# ---++ AutoRedirectPlugin
# This is the configuration used by the <b>AutoRedirectPlugin</b>.

# **PERL CHECK="undefok emptyok"**
# Rules to trigger a redirect.
$Foswiki::cfg{Plugins}{AutoRedirectPlugin}{Rules} = [
  {
    'target' => 'none',
    'context' => 'register',
  },
  {
    "target" => "Main.WebHome",
    "web" => "Applications.*",
    "wikiName" => "WikiGuest",
  },
  {
    "target" => "Main.WebHome",
    "topic" => "(Web|Site)Preferences",
    "wikiName" => "WikiGuest",
  },
  {
    "target" => "none",
    "topic" => 'UserRegistration|ResetPassword|ChangeEmailAddress|ChangePassword',
    "web" => "System",
  },
  {
    "target" => "Main.WebHome",
    "web" => "System",
    "wikiName" => "WikiGuest",
  },
];

1;
