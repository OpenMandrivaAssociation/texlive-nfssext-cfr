# revision 19322
# category Package
# catalog-ctan /macros/latex/contrib/nfssext-cfr
# catalog-date 2010-06-30 12:36:12 +0200
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-nfssext-cfr
Version:	1.2
Release:	1
Summary:	Extensions to the LaTeX NFSS
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nfssext-cfr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nfssext-cfr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nfssext-cfr.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package is a development of nfssext.sty, distributed with
the examples for the font installation guide. The package has
been developed for use in packages such as cfr-lm and
venturisadf,.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/nfssext-cfr/nfssext-cfr.sty
%doc %{_texmfdistdir}/doc/latex/nfssext-cfr/README
%doc %{_texmfdistdir}/doc/latex/nfssext-cfr/nfssext-cfr.pdf
%doc %{_texmfdistdir}/doc/latex/nfssext-cfr/nfssext-cfr.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
