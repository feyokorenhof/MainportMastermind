#!/usr/local/bin/php
<?php
define('DIR', 'tree');
define('FILE', 'blob');

function main() {
	$root_object = 'b32afd3';
	restore_object($root_object, 'restored');
}

function restore_object($object, $dest) {
	$type = get_object_type($object);

	if ($type == FILE) {
		echo 'restoring ' . $dest . "\n";
		shell_exec('git cat-file -p ' . $object . ' > ' . $dest);
	} else {
		echo 'restoring ' . $dest . "\n";
		mkdir($dest);
		restore_directory($object, $dest);
	}
}

function restore_directory($object, $base_dest) {
	$files = parse_tree_object($object);

	foreach ($files as $file) {
		restore_object($file['object'], $base_dest . '/' . $file['name']);
	}
}

function parse_tree_object($object) {
	if (DIR != get_object_type($object)) {
		throw new Exception("Trying to decode TREE object, but BLOB given: {$object}");
	}

	$contents = read_object($object);

	$tree = [];
	$lines = explode("\n", trim($contents));
	foreach ($lines as $branch) {
		$leaves = preg_split("#\s+#", $branch, 4);

		$tmp = [
			'mode' => $leaves[0],
			'type' => $leaves[1],
			'object' => $leaves[2],
			'name' => $leaves[3],
		];

		array_map('trim', $tmp);
		$tree[] = $tmp;
	}

	return $tree;
}

function read_object($object) {
	$contents = trim(shell_exec('git cat-file -p ' . $object));
	return $contents;
}

function get_object_type($object) {
	$type = shell_exec("git cat-file -t {$object}");
	return trim($type);
}

main();