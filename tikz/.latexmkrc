use Cwd qw(cwd);
use File::Spec;
my $dir = cwd;
$lv = "lehre-chemie-msr";
if (index($dir, $lv) != -1) {
	my ($path, $dummy) = split /$lv/, $dir;
	$ENV{'TEXMFHOME'} = File::Spec->catfile($path, $lv, "texmf");
}

$pdflatex = 'pdflatex --shell-escape %S';
push @generated_exts, 'synctex', 'synctex.gz';
$clean_ext .= ' %R.ist %R.xdy %R.bbl';
