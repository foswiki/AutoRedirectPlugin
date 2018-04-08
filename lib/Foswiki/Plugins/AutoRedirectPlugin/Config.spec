# ---+ Extensions
# ---++ AutoRedirectPlugin
# This is the configuration used by the <b>AutoRedirectPlugin</b>.

# **PERL CHECK="undefok emptyok"**
# Rules to trigger a redirect.
$Foswiki::cfg{Plugins}{AutoRedirectPlugin}{Rules} = [
  {
    "context" => "view",
    "web" => "Sandbox",
    "topic" => "AutoRedirectTest",
    "target" => "Main.WebHome",
  },
  {
    "wikiName" => "WikiGuest",
    "web" => "Applications.*",
    "target" => "Main.WebHome",
  },
  {
    "web" => "System",
    "topic" => 'UserRegistration|ResetPassword|ChangeEmailAddress|ChangePassword',
    "target" => "none",
  },
  {
    "web" => "System",
    "wikiName" => "WikiGuest",
    "target" => "Main.WebHome",
  },
];

1;
