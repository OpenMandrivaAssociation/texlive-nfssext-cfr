Name:		texlive-nfssext-cfr
Version:	43640
Release:	2
Summary:	Extensions to the LaTeX NFSS
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nfssext-cfr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nfssext-cfr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nfssext-cfr.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is a development of nfssext.sty, distributed with
the examples for the font installation guide. The package has
been developed for use in packages such as cfr-lm and
venturisadf,.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/nfssext-cfr/nfssext-cfr.sty
%doc %{_texmfdistdir}/doc/latex/nfssext-cfr/README
%doc %{_texmfdistdir}/doc/latex/nfssext-cfr/nfssext-cfr.pdf
%doc %{_texmfdistdir}/doc/latex/nfssext-cfr/nfssext-cfr.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
