{}:

let
  hashes = import ./hashes.nix;
  # nixos-24.05
  ref = "d8b181dd128acec263e762cfac473ebb0fdd9a5e";
  hash = "0pni5a8nb822611n23iyaqhjlqgcv7lwck12l3s5i6mnsw3slslh";

  fetchCommit = fetchTarball {
    url = "https://github.com/NixOS/nixpkgs/archive/${ref}.tar.gz";
    sha256 = "${hash}";
  };
in

# Keep line 12 as it is! Only modify it by running update-default-nix.py. The updating script depends on the next line being as it is on line 12.
import fetchCommit { }
