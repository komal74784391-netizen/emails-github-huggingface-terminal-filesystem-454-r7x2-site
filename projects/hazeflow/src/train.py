import argparse
from models.haze_net import HazeNet


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', required=True)
    args = parser.parse_args()
    model = HazeNet.from_config(args.config)
    model.fit()


if __name__ == '__main__':
    main()
