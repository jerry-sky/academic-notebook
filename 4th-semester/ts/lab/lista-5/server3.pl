#!/usr/bin/perl
use HTTP::Daemon;
use HTTP::Status;

my $d = HTTP::Daemon->new || die;
print "Please contact me at: \nhttp://localhost:", $d->sockport(), "/a\n";

while (my $c = $d->accept) {
  while (my $r = $c->get_request) {
    if ($r->method eq 'GET' and $r->uri->path eq "/a") {

      $file_s = "./readme.md";
      $c->send_file_response($file_s);

    }
    else {
      $c->send_error(RC_FORBIDDEN)
    }
  }
  $c->close;
  undef($c);
}
