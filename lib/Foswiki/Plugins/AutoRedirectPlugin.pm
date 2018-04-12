# Plugin for Foswiki - The Free and Open Source Wiki, https://foswiki.org/
#
# AutoRedirectPlugin is Copyright (C) 2018 Michael Daum http://michaeldaumconsulting.com
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details, published at
# http://www.gnu.org/copyleft/gpl.html

package Foswiki::Plugins::AutoRedirectPlugin;

use strict;
use warnings;

use Foswiki::Func ();

our $VERSION = '1.01';
our $RELEASE = '12 Apr 2018';
our $SHORTDESCRIPTION = 'automatically redirect a set of topics';
our $NO_PREFS_IN_TOPIC = 1;

use constant TRACE => 0;

sub initPlugin {
  my ($topic, $web) = @_;

  my $rules = $Foswiki::cfg{Plugins}{AutoRedirectPlugin}{Rules} || [];

  my $target;
  my $context = Foswiki::Func::getContext();
  my $wikiName = Foswiki::Func::getWikiName();
  foreach my $rule (@$rules) {

    if ( (!$rule->{context} || $context->{$rule->{context}})
      && (!$rule->{wikiName} || $wikiName =~ /^(?:$rule->{wikiName})$/)
      && (!$rule->{web} || $web =~ /^(?:$rule->{web})$/)
      && (!$rule->{topic} || $topic =~ /^(?:$rule->{topic})$/))
    {
      $target = $rule->{target};
      last;
    }
  }

  if ($target && $target ne '' && $target ne 'none') {
    my $url;
    if ($target =~ /^https?:/) {
      $url = $target;
      print STDERR "MATCH: redirecting to $$url\n" if TRACE;
    } else {
      my ($targetWeb, $targetTopic) = Foswiki::Func::normalizeWebTopicName($web, $target);
      $url = Foswiki::Func::getScriptUrl($targetWeb, $targetTopic, 'view');
      print STDERR "MATCH: redirecting to $targetWeb.$targetTopic ($url)\n" if TRACE;
    }

    my $query = Foswiki::Func::getRequestObject();
    Foswiki::Func::setPreferencesValue('COVER', 'plain'); # to fasten the rest of the rendering process
    Foswiki::Func::redirectCgiQuery($query, $url);

  } else {
    print STDERR "No rule matches to perform an auto redirect for $web.$topic, $wikiName\n" if TRACE;
  }

  return 1;
}

1;
