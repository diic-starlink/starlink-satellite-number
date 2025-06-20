let
  pkgs = import ./nixpkgs {};
in pkgs.mkShell {
  pname = "satellite-development";
  version = "0.0.1";

  buildInputs = with pkgs; [
    poetry
  ];
}

